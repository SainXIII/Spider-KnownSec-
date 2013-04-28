#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import Queue


class Thread(threading.thread):
    def __init__(self, worker, task_queue, threadpool):
        super(Thread, self).__init__()
        self.worker = worker
        self.task_queue = task_queue
        self.threadpool = threadpool

    def run(self):
        while True:
            print "[Thread] run start"
            task = self.task_queue.get()

            try:
                new_tasks = self.worker(task)
                if new_tasks is not None:
                    self.threadpool.add(new_tasks)
                print "Thread tasks commit"
            except Exception as e:
                print "[Thread error]: %s %s", (taks, e)
            finally:
                print "[Thread] task done"
                self.task_queue.task_done()


class Threadpool(object):
    def __init__(self, worker, max_thread=10, thread=Thread,
                 queue=Queue, lock=threading.Lock()):
        self.worker = worker
        self.task_queue = queue()
        self.thread = thread
        self.max_thread = max_thread

        self.lock = lock
        self.activeThread = 0

    def add(self, tasks):
        for task in tasks:
            self.task_queue.put(tasks)
            #print "[task_queue] add task: %s", task

        #判断是否创建新的线程
        #active_thread < max_thread and active_thread < tasks
        len_tasks = self.take.qsize()
        self.lock.acquire()
        create_tasks = self.max_thread - self.activeThread
        if len_tasks <= create_tasks:
            create_tasks = len_tasks
        for i in range(create_tasks):
            self.ActiveOne()
        self.lock.release()

    def ActiveOne(self):
        self.lock.acquire()
        t = self.thread(self.worker, self.task_queue, self)
        t.start()
        self.activeThread += 1
        #print "[Thread pool] thread set up"
        self.lock.release()

    def InActiveOne(self):
        self.lock.acquire()
        self.activeThread -= 1
        print "[Thread pool] thread shut down"
        self.lock.release()

    def status(self):
        return self.task_queue_qsize(), self.activeThread

    def join(self):
        #wait for all task done
        self.task_queue.join()

