#!/usr/bin/env python
# -*- coding:utf-8 -*-

__all__ = ['logger']

import logging

LOG_FOR = {
	1: {"format": "%(asctime)s %(name)s %(link)s %(http_status)s"},
	2: {"format": "%(asctime)s %(name)s %(link)s %(http_status)s %(content_size)s"},
	3: {"format": "%(asctime)s %(name)s %(link)s %(http_status)s %(content_size)s %(server)s"},
	4: {"format": "%(asctime)s %(name)s %(link)s %(http_status)s %(content_size)s %(server)s %(last_modified)s"},
	5: {"format": "%(asctime)s %(name)s %(link)s %(http_status)s %(content_size)s %(server)s %(last_modified)s %(start_time)s %(end_time)s"},
}


LOG_DIC = {
	"version": 1,
	"formatters": {
		"logfile_frm": {
			"format": "%(levelname)s %(threadName)-15s%(filename)-15s%(module)+10s.%(funcName)-10s%(asctime)-25s%(message)s",
		},
		"display": {
			"format": "%(message)s",
		},
	},
	
	"handlers": {
		"logfile_hld": {
			"class": "logging.FileHandler",
			"filename": "spider.log",
			"formatter": "logfile_frm",
			"level": "DEBUG",
		},
		"display": {
			"class": "logging.StreamHandler",
			"formatter": "display",
			"level": "INFO",
		}
	},
	
	"loggers": {
		"spider": {
			"level": "DEBUG",
			"handlers": ["hld",],
		},
		"term": {
			"level": "INFO",
			"handlers": ["display",],
		},
	},
}

def logger(logfile="spider.log", level=1):
	if not 1 <= level <= 5:
		raise Exception("[args error]: 1 <= level <= 5")
		
	LOG_DIC["handlers"]["logfile_hld"]["filename"] = logfile
	LOG_DIC["handlers"]["logfile_hld"]["level"] = logging.getLevelName(level*10)
	LOG_DIC["formatters"]["logfile_fmt"]["format"] = LOR_FMT[level]
	
	logging.config.dicConfig(LOG_DIC)
		
