#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import urllib2

class Linkpool(object):
	"""
	Linkpool用于处理已经抓取的链接,过滤出属于同一网站的所有links

	>>> l = Linkpool(4)
	>>> l.filter("http://blog.knownsec.com", ["http://www.baidu.com", "http://www.qq.com"]) #doctest +NORMALIZE_WHITESPACE
	[]

	>>> l.filter("http://blog.knownsec.com", ["http://www.knownsec.com", "http://blog.knownsec.com/about/"]) #doctest +NORMALIZE_WHITESPACE
	['http://blog.knownsec.com/about/']
	"""
	def __init__(self, depth, lock=threading.RLock()):
		self.lock = lock
		self.depth = depth
		self.linked = {} 

	def addlink(self, link, depth):
		self.lock.acquire()
		self.linked[link] = depth
		self.lock.release()
		
	def status(self):
		return len(self.linked)

	def filter(self, baseurl, urls):
		"""
		.过滤非本站的链接
		.过滤已经爬过的链接
		"""
		#print '|||||||||||||||||||||||', threading.currentThread()
		#print "Filter: %s has %s links" % (baseurl, len(urls))
		if len(self.linked) == 0:
			self.addlink(baseurl, 0)
			self.host = urllib2.Request(baseurl).get_host()
		depth = self.linked[baseurl]
		#print "links: %s, depth: %s" % (baseurl, depth-1)
		if depth >= self.depth:
			return []
		# 过滤非本站的链接
		Turl = []
		for i in urls:
			host = urllib2.Request(i).get_host()
			if self.host == host:
				Turl.append(i)
		# 过滤已经爬过的链接
		#print '|||||||||||||||||||||||', threading.currentThread(), Turl
		newlinks = []
		for i in Turl:
			self.lock.acquire()
			if self.linked.has_key(i):
				self.lock.release()
				continue
			else:
				newlinks.append(i) 
				self.addlink(i, depth+1)
			self.lock.release()
		#print '|||||||||||||||||||||||', threading.currentThread(), Turl
		return newlinks

if __name__ == "__main__":
	import doctest
	doctest.testmod()
