#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging

LOG_FOR = {
	"10": {"format": "%(asctime)s %(name)s %(link)s %(http_status)s"},
	"20": {"format": "%(asctime)s %(name)s %(link)s %(http_status)s %(content_size)s"},
	"30": {"format": "%(asctime)s %(name)s %(link)s %(http_status)s %(content_size)s %(server)s"},
	"40": {"format": "%(asctime)s %(name)s %(link)s %(http_status)s %(content_size)s %(server)s %(last_modified)s"},
	"50": {"format": "%(asctime)s %(name)s %(link)s %(http_status)s %(content_size)s %(server)s %(last_modified)s %(start_time)s %(end_time)s"},
}


LOG_DIC = {
	"version": 1,
	"formatters": {
		"logfile_frm": {
			"format": "%(levelname)s %(threadName)-15s%(filename)-15s%(module)+10s.%(funcName)-10s%(asctime)-25s%(message)s"，
		},
		"display": {
			"format": "%(message)s"，
		}
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
	
	logging.config.dicConfig(LOG_DIC)
		
