#!/usr/bin/env python
# -*- coding:utf-8 -*-

__all__ = ['argsparse']

import argparse
import sys

def argsparse(arg):
	"""
	参数解析
	
	>>> input = "-u example.com -d 2 -f spider.log -l 3 --thread 3 --dbfile spider.db --key Web".split()
	>>> print argsparse(input)
	Namespace(d=2, dbfile='spider.db', f='spider.log', key='Web', l=3, testself=None, thread=3, u='example.com')
	"""
	parser = argparse.ArgumentParser(description="The usage of spider(KnownSec)")
	parser.add_argument("-u", dest="url", metavar="URL", help="The url of Web site")#, required=True)
	parser.add_argument("-d", dest="depth", metavar="Depth", help="The Depth", type=int)#, required=True)
	parser.add_argument("-f", dest="logfile", metavar="Logfile", help="Log file", default="spider.log")
	parser.add_argument("-l", dest="loglevel", metavar="LogLevel", help="Log level(1-5)", type=int, choices=xrange(1,6), default=3)
	parser.add_argument("--thread", metavar="threads", help="The number of threads", type=int, default=10)
	parser.add_argument("--dbfile", metavar="dbfile", help="DB file name")#, required=True)
	parser.add_argument("--key", metavar="key", help="The key word")
	parser.add_argument("--testself", help="Self test", action="store_true", default=False)
	
	args = parser.parse_args(arg)
	if not args.testself and (not args.url or not args.depth or not args.dbfile):
		print "-u -d --dbfile is necessary"
		sys.exit(0)

	return args

if __name__ == "__main__":
	import doctest
	print doctest.testmod()

