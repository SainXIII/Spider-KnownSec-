#!/usr/bin/env python
# -*- coding:utf-8 -*-

import fetch

if __name__ == "__main__":
    job = fetch.Fetch("www.ouc.edu.cn/index.htm", 1)
    job.work()
