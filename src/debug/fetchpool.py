#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import threading

"""
def fetcher(analysis, linkpool):
    def fetch(link):
        #print link, "=========================="
        link = link if link.startswith("http://") else "http://" + link
        #print link, "==========================="
        urlobj = isOK(link)
        #print 'URL: %s' % urlobj.get_url
        if urlobj is None:
            return []
        content = urlobj.read()
        analysis.find_keyword(link, content)
        links = analysis.fetch_links(link, content)
        newlinks = linkpool.filter(link, links)

        return newlinks
    return fetch
"""

class fetchpool(object):
    def __init__(self, analysis, linkpool):
        self.analysis = analysis
        self.linkpool = linkpool

    def fetcher(self):
        def fetch(link):
            link = link if link.startswith("http://") else "http://" + link
            urlobj = isOK(link)
            if urlobj is None:
                return []
            content = urlobj.read()
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
        urlobj = urllib2.urlopen(url, timeout=3)
    except (ValueError, urllib2.URLError):
        print "(Log: URL Error)"
        return None
    if urlobj.code >= 400:
        print "(Log: Can't visit site)"
        return None
    return urlobj
        
