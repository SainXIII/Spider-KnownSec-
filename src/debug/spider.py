#!/usr/bin/env python
# -*- coding:utf-8 -*-

from fetchpool import fetchpool
from analysis import Analysis
from threadpool import Thread, Threadpool
from linkpool import Linkpool

if __name__ == "__main__":
    tasks = ["http://it.ouc.edu.cn/Default.aspx", ]
    analysis = Analysis()
    linkpool = Linkpool(depth=2)
    fetchpool = fetchpool(analysis, linkpool)
    threadpool = Threadpool(fetchpool.fetcher())
    threadpool.add(tasks)
    threadpool.join()

