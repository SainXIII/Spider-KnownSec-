#!/usr/bin/env python
#-*- coding:utf-8 -*-

__all__ = ['Status']

import threading
import time
import logging

class Status(object):
	"""
	控制terminal端显示
	"""
	def __init__(self, threadpool, linkpool):
		self.threadpool = threadpool
		self.linkpool = linkpool
		
	def currentStatus(self):
		"""
		显示当前的状态
		"""
		while True:
			if self.threadpool.activeThread == 0:
				print "all is over"
				break
			task, thread = self.threadpool.status()
			ctotal = self.linkpool.status()
			print "Current Task: %s  Current Thread: %s total(fetched): %s" % (task, thread, ctotal)
			time.sleep(2)
	
	def display(self):
		t = threading.Thread(target=self.currentStatus)
		t.start()
