#!/usr/bin/env python
# -*- coding:utf-8 -*-

__all__ = ['tester']

from os import popen

def tester():
	files = ["analysis.py", "fetchpool.py", "linkpool.py", "argsparse.py"]
	for file in files:
		res = popen("python %s" % file).read()
		print res

	