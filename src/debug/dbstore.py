#!/usr/bin/env python
# -*- coding:utf -*-

__all__ = ["Storepool"]

import sqlite3
import threading
import logging
import os.path

class Storepool(object):
	"""
	"""
	def __init__(self, db="spider.db", lock=threading.RLock()):
		self.conn = sqlite3.connect(db, check_same_thread=False)
		self.lock = lock
		self.createtable()

	def createtable(self):
		with self.conn:
			self.conn.executescript("""
				create table if not exists tasks(
					id integer primary key autoincrement,
					task text not null
				);

				create table if not exists keyword(
					id integer primary key autoincrement,
					url text not null,
					keyword text not null default 'None'
				);
			""")

	def inserttasks(self, url):
		sql = "insert into tasks \
				(url) values ('?');"
		para = (url,)
		with self.conn:
			self.conn.execute(sql, para)

	def store(self, url, keyword=None):
		self.lock.acquire()
		sql = "insert into keyword \
				(url, keyword) values (?, ?);"
		para = (url, keyword)
		with self.conn:
			self.conn.execute(sql, para)
		#print "--------", url, keyword
		self.lock.release()
        
        
