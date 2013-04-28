#!/usr/bin/env python
# -*- coding:utf-8 -*-

from analysis import Analysis
from linkpool import Linkpool

import urllib2

def fetchpool(analysis, linkpool):
    """
    fetchpool用于粘和页面分析和链接处理功能。
    页面分析和链接处理是fetcher公共使用的.
    """
    def fetcher(link):
        link = link if link.startswith("http://") else "http://" + link
        urlobj = isOK(link)
        if urlobj is None:
            return []

        analysis.find_keyword(link, urlobj.read())
        links = analysis.fetch_links(link, urlobj.read())
        newlinks = linkpool.filter(link, links)

        return newlinks
    return fetcher
        
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
    
