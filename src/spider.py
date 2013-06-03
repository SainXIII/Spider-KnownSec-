#!/usr/bin/env python
# -*- coding:utf-8 -*-

from fetchpool import Fetchpool
from analysis import Analysis
from threadpool import Thread, Threadpool
from linkpool import Linkpool
from dbstore import Storepool
from display import Status
from argsparse import argsparse
from logger import logger
from tester import tester

from sys import argv, exit

if __name__ == "__main__":
	args = argsparse(argv[1:])
	
	url = args.url
	depth = args.depth
	logfile = args.logfile
	loglevel = args.loglevel
	dbfile = args.dbfile
	threads = args.thread
	key = args.key
	testself = args.testself
	
	
	if testself is True:# 程序自测
		tester()
		exit(1)
	
	tasks = [url,]
	logger(logfile, loglevel)# 启动日志
	
	dbpool = Storepool(dbfile)# 启动数据库
	dbpool.createtable()
	
	analysis = Analysis(dbpool, keyword)# 启动页面分析模块
	linkpool = Linkpool(depth=depth)# 启动链接管理池
	fetchpool = Fetchpool(analysis, linkpool)# 启动爬虫工厂
	threadpool = Threadpool(fetchpool.fetcher())# 建立线程池
	threadpool.add(tasks)# 添加任务
	status = Status(threadpool, linkpool)# 创建状态反馈模块
	status.display()# 启动状态反馈模块
	
	threadpool.join()# 等待任务结束
	"""
	tasks = ["http://it.ouc.edu.cn/Default.aspx", ]
	dbpool = Storepool('test')
	dbpool.createtable()
	analysis = Analysis(dbpool, '中国')
	linkpool = Linkpool(depth=1)
	fetchpool = Fetchpool(analysis, linkpool)
	threadpool = Threadpool(fetchpool.fetcher())
	threadpool.add(tasks)
	print threadpool.status()
	status = Status(threadpool, linkpool)
	status.display()
	threadpool.join()
"""
