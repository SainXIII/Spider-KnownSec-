#!/usr/bin/env python
# -*- coding:utf-8 -*-

from analysis import Analysis
from linkpool import Linkpool

import urllib2

class fetchpool(object):
    """
    fetchpool用于粘和页面分析和链接处理的功能.
    """
    def __init__(self, analysis, linkpool):
        """
        analysis和linkpool两个公共的功能
        """
        self.analysis = anslysis
        self.linkpool = linkpool

    def fetcher(self, link):
        link = link if link.startswith("http://") else "http://" + link
        urlobj = self.isOK(link)
        if urlobj is None:
            return []

        self.analysis.find_keyword(link, urlobj.read())
        links = self.analysis.fetch_links(link, urlobj.read())
        newlinks = self.linkpool.filter(link, links)

        return newlinks
        
    def isOK(self, url):
        """
        判断页面使用可以打开以及正确性
        """
        try:
            urlobj = urllib2.urlopen(url)
        except (ValueError, urllib2.URLError):
            print "(Log: URL Error)"
            return None
        if urlobj.code >= 400:
            print "(Log: Can't visit site)"
            return None
        return urlobj
        
