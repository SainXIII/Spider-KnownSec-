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

    >>> Analysis() #doctest: +ELLIPSIS 
    <....Analysis object at 0x...>

    >>> Analysis("db") #doctest: +ELLIPSIS 
    <....Analysis object at 0x...>

    >>> Analysis("db", "keyword") #doctest: +ELLIPSIS 
    <....Analysis object at 0x...>

    >>> a = Analysis()
    >>> a.fetch_links("http://example.com", "<a href='test1'>test1</a><a href='/test2'>test2</a> \
            <a href='http://test.com/test3'>test3</a><a href='http://example.com/test4/test4'>test4</a> \
            <a href='http://example.com/test5'>test5</a><a href='mailto:test6@mail.com'>test6</a>") #doctest: +NORMALIZE_WHITESPACE
    [u'http://example.com/test1', u'http://example.com/test2', u'http://test.com/test3', u'http://example.com/test4/test4', \
    u'http://example.com/test5', u'mailto:test6@mail.com']

    """ 
    def __init__(self, dbsave = None, keyword = None):
        self.dbsave = dbsave
        self.keyword = keyword

    def fetch_links(self, baseurl, content):
        """
        从urllib2打开的对象中过滤出所有的link, 返回url列表
        """
        content = BeautifulSoup(content)
        links = [ link.get("href") for link in content.findAll(re.compile("^(a|A)")) ]
        urls = []
        for url in links:
            if type(url) == type(None):
                continue
            url = self.unify_url(baseurl, url)
            if url is None:
                continue
            #flag
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

    def find_keyword(self, link, content):
        """
        在网页中寻找关键字，若存在返回url，否则返回None
        """
        d = {'keyword' : self.keyword, 'url' : link}
        reo = re.compile(re.escape(self.keyword))
        if reo.search(content) is not None:
            return d
        return None
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()
