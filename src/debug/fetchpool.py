#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import threading
import chardet


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
        print url
        urlobj = urllib2.urlopen(url, timeout=5)
    except (ValueError, urllib2.URLError) as e:
        print "(Log: URL Error)", e
        return None
    if urlobj.code >= 400:
        print "(Log: Can't visit site)"
        return None
    return urlobj
        
def codec(content):
    code = chardet.detect(content)["encoding"]
    if code in ["GB2312", "GBK"]:
        code = "GB2312"
    elif code is None:
        return content
    c = content.decode(code).encode("utf-8")
    return c
