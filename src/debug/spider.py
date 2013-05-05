#!/usr/bin/env python
# -*- coding:utf-8 -*-

from fetchpool import Fetchpool
from analysis import Analysis
from threadpool import Thread, Threadpool
from linkpool import Linkpool
from dbstore import Storepool

if __name__ == "__main__":
    tasks = ["http://it.ouc.edu.cn/Default.aspx", ]
    dbpool = Storepool('test')
    dbpool.createtable()
    analysis = Analysis(dbpool, '中国')
    linkpool = Linkpool(depth=1)
    fetchpool = Fetchpool(analysis, linkpool)
    threadpool = Threadpool(fetchpool.fetcher())
    threadpool.add(tasks)
    threadpool.join()

