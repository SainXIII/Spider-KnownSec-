#!/usr/bin/env python
# -*- coding:utf-8 -*-

__all__ = []

from analysis import Analysis
from Queue import Queue
import urllib2

class Fetch(object):
    """
    根据url和深度抓取links
    """
    def __init__(self, url, depth = 0):
        self.jobs = Queue()
        self.maxdepth = depth
        self.fetced_urls = []
        self.jobs.put((url, 0))
        self.analysis = Analysis()

    def work(self):
        while True:
            if self.jobs.empty():
                break
            url, depth = self.jobs.get()
            self.fetch(url, depth+1)

    def fetch(self, url, depth):
        if depth > self.maxdepth:
            return
        urlobj = self.isOK(url) 
        if urlobj is None
            return 
        #判断页面是否正确，判断url是否正确
        #analysis = Analysis()
        urls = self.analysis.fetch_links(url, urlobj)
        self.add_job(urls, depth)

    def add_job((self, urls, depth):
        for url in urls:
            if url not in self.fetched_urls:
                self.jobs.put((url, depth))

    def isOK(self, url):
        """
        判断url链接是否可以打开,及正确性
        """
        try:
            urlobj = urllib2.urlopen(url)
        except ValueError, URLError:
            return None
        if urlobj.code >= 400:
            return None
        return urlobj

