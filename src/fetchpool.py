#!/usr/bin/env python
# -*- coding:utf-8 -*-

__all__ = ['Fetchpool', 'isOK', 'codec']

import urllib2
import threading
import chardet
import logging

log_spider = logging.getLogger("spider")

class Fetchpool(object):
	def __init__(self, analysis, linkpool):
		self.analysis = analysis
		self.linkpool = linkpool

	def fetcher(self):
		def fetch(link):
			link = link if link.startswith("http://") else "http://" + link
			urlobj = isOK(link)
			if urlobj is None:
				return []
			content = codec(urlobj.read())
			self.analysis.find_keyword(link, content)
			links = self.analysis.fetch_links(link, content)
			newlinks = self.linkpool.filter(link, links)
			#print threading.currentThread(), "============================="
			#print 'In fetchpool %s' % threading.currentThread()
			return newlinks
		return fetch

def isOK(url):
	"""
	判断页面使用可以打开以及正确性
	"""
	try:  
		#print url
		urlobj = urllib2.urlopen(url, timeout=20)
	except (ValueError, urllib2.URLError) as e:
		log =  "(Log: URL Error)", e
		# print log
		log_spider.debug(log)
		return None
	if urlobj.code >= 400:
		print "(Log: Can't visit site)"
		log_spider.debug("(Log: Can't visit site)")
		return None
	return urlobj
        
def codec(content):
	"""
	调整page的编码，（附加）...
	"""
	code = chardet.detect(content)["encoding"]
	if code in ["GB2312", "GBK"]:
		code = "GB2312"
	elif code is None:
		return content
	c = content.decode(code).encode("utf-8")
	return c
