#!/usr/bin/env python
#-*- coding:utf-8 -*-

__all__ = ['Status']

import threading
import time
import logging

log_term = logging.getLogger("term")

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
				log_term.info("Mission is complete!!!")
				break
			task, thread = self.threadpool.status()
			ctotal = self.linkpool.status()
			msg = "Current Task: %s  Current Thread: %s total(fetched): %s" % (task, thread, ctotal)
			log_term.info(msg)
			time.sleep(10)
	
	def display(self):
		t = threading.Thread(target=self.currentStatus)
		t.start()
