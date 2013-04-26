#!/usr/bin/env python
# -*- coding:utf-8 -*-

__all__ = ["Analysis"]

from BeautifulSoup import BeautifulSoup
import urlparse
import urllib2
import logging
import datetime
import re

class Analysis(object):
    """ 
    分析page,过滤出所有的链接，并对链接进行处理。
    """ 
    def __init__(self, dbsave = None, keyword = None):
        self.dbsave = dbsave
        self.keyword = keyword

    def fetch_links(self, baseurl, urlobj):
        """
        从urllib2打开的对象中过滤出所有的link, 返回url列表
        """
        content = Beautiful.Soup(urlobj.read())
        links = [ link.get("href") for link in content.findAll(re.compile("^(a|A)")) ]
        urls = []
        for url in links:
            if type(url) == type(None):
                continue
            url = self.unify_url(baseurl, url)
            if url is None:
                continue
            #flag
            print "----->", url
            urls.append(url)
        return urls
    
    def unify_url(self, baseurl, newurl):
        """
        处理所有的links
        scheme://username:password@netloc:port/path;param?query=arg#fragment
        """
        url = newurl.strip() #去除空格
        url = url.split('#')[0]
        if len(url) == 0:
            return None
        url = urlparse.urljoin(baseurl, url)
        return url

    def find_keyword(self, urlobj):
        """
        在网页中寻找关键字，若存在返回url，否则返回None
        """
        d = {'keyword' : self.keyword, 'url' : urlobj.url}
        reo = re.compile(re.escape(self.keyword))
        if reo.search(urlobj.read()) is not None:
            return d
        return None
        
        
