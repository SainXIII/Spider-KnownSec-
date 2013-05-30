#!/usr/bin/env python
#-*- coding:utf-8 -*-

import threading
import time
import logging

def currentStatus(threads, linkm, queue, timeout=1):
    """
    显示当前的状态
    """
    while True:
        _, 