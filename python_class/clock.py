#!/usr/bin/python3
# -*- coding:utf-8 -*-

from time import sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """"初始化方法
        :param hour:时
        :param minute:分
        :param second:秒
        """
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        """走字"""
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        return '%02d:%02d:%02d' % \
               (self.hour, self.minute, self.second)


def main():
    clock = Clock(22, 45, 38)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
