# 概要设计文档  

## Spider功能:  
+ 指定网站爬行
 1. 指定开始地址
 2. 指定深度
 3. 关键字查找  
+ 数据库存储  
 1. 爬行结果记录  
+ 日志文件记录  
 1. 指定等级日志
 2. 指定日志文件存储路径  
+ 线程池  
+ 测试单元  

## Spider所需Modules:  
+ urllib/urllib2
+ beautifulsoup
+ threading
+ Queue
+ sqlite3
+ logger
+ doctest
+ argparse  

## Spider模块  
    analysis
    fetch
    threadpool
    logger
    dbfile
    test  


