# -*- codeing = UTF-8 -*-
# @Time : 2021/1/17 14:48
# @Author : 马增龙 15634099385
# @File : exp5.1.py
# @Software : PyCharm
import time
class Timer:
    def __init__(self):
        self.info = '未开始计时!'
        self.startTime = None
        self.endTime = None
        self.jg = 0
    def getstartTime(self):
        return self.startTime

    def getendTime(self):
        return self.endTime

    def start(self):
        self.startTime = time.time()

    def stop(self):
        self.endTime = time.time()

    def getTimePeriod(self):
        self.jg = self.getendTime() - self.getstartTime()
        self.jg = self.jg * 1000
        self.info = '共运行了%d毫秒' % self.jg
        return self.jg


def main():
    t1 = Timer()
    t1.start()
    for i in range(1, 1000001):
        pass
    t1.stop()
    t1.getTimePeriod()
    print(t1.info)

    t2 = Timer()
    t2.start()
    sum = 0
    for i in range(1, 1000001):
        sum = sum + i
    t2.stop()
    t2.getTimePeriod()
    print(t2.info)

    main()

