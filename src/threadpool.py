#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
from Queue import Queue
import logging

log_spider = logging.getLogger("spider")
log_term = logging.getLogger("term")

class Thread(threading.Thread):
	def __init__(self, worker, task_queue, threadpool):
		super(Thread, self).__init__()
		self.worker = worker
		self.task_queue = task_queue
		self.threadpool = threadpool

	def run(self):
		while True:
			# print self.threadpool.status()
			# print self.task_queue.qsize()
			if self.task_queue.empty():
				self.threadpool.InActiveOne()
				# print "InActiveOne() %s" % threading.currentThread()
				break
			# print "[Run Start] %s" % threading.currentThread()
			task = self.task_queue.get()
			# print "[Job: %s  + %s]" % (task, threading.currentThread())
			try:
				new_tasks = self.worker(task)
				log_spider.debug(threading.currentThread())
				# print threading.currentThread(), new_tasks
				# log_term.info("%s %s" % (threading.currentThread(), new_tasks))
				if new_tasks is not None:
					self.threadpool.add(new_tasks)
				# print "[tasks commit] %s" % threading.currentThread()
			except Exception as e:
				log_spider.debug("[Thread error]: %s %s" % (task, e))
				# logger.debug("[Thread error]: %s %s" % (task, e))
			finally:
				# if new_tasks is not None:
				# self.threadpool.add(new_tasks)
				# print "[task done] %s" % threading.currentThread()
				# print "finish %s %s" % (task, threading.currentThread())
				# print "task_queue task_done() ++ %s" % threading.currentThread()
				self.task_queue.task_done()


class Threadpool(object):
	def __init__(self, worker, max_thread=10, thread=Thread,\
				 queue=Queue, lock=threading.RLock()):
		self.worker = worker
		self.task_queue = queue()
		self.thread = thread
		self.max_thread = max_thread

		self.lock = lock
		self.activeThread = 0

	def add(self, tasks):
		# print tasks
		for task in tasks:
			self.task_queue.put(task)
		#    print "[add task]: %s"% task

		# 判断是否创建新的线程
		# active_thread < max_thread and active_thread < tasks
		len_tasks = self.task_queue.qsize()
		self.lock.acquire()
		create_tasks = self.max_thread - self.activeThread
		if len_tasks <= create_tasks:
			create_tasks = len_tasks
		for i in range(create_tasks):
			self.ActiveOne()
		self.lock.release()

	def ActiveOne(self):
		self.lock.acquire()
		t = self.thread(self.worker, self.task_queue, self)
		t.start()
		self.activeThread += 1
		# print "[set up] %s" %\
		#        threading.currentThread()
		self.lock.release()
 
	def InActiveOne(self):
		self.lock.acquire()
		self.activeThread -= 1
		# print "[shut down]%s" %\
		#        threading.currentThread()
		self.lock.release()
 
	def status(self):
		return self.task_queue.qsize(), self.activeThread

	def join(self):
		# wait for all task done
		self.task_queue.join()

