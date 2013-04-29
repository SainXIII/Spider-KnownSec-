#!/usr/bin/env python
# -*- coding:utf-8 -*-

from fetchpool import fetchpool
from analysis import Analysis
from threadpool import Thread, Threadpool
from linkpool import Linkpool

if __name__ == "__main__":
    tasks = ["http://www.ouc.edu.cn/index.htm", ]
    analysis = Analysis()
    linkpool = Linkpool(depth=3)
    fetchpool = fetchpool(analysis, linkpool)
    threadpool = Threadpool(fetchpool.fetcher())
    threadpool.add(tasks)
    threadpool.join()

