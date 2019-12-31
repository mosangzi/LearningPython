#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')

    def watch_movie(self):
        if self.age < 18:
            print(f'{self.name}只能看动画片')
        else:
            print(f'{self.name}可以看18+电影')

