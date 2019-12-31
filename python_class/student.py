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


def run():
    stu1 = Student('John', 35)
    stu1.study('算法导论')
    stu1.watch_movie()
    stu2 = Student('王大锤', 17)
    stu2.study('立体几何')
    stu2.watch_movie()


if __name__ == '__main__':
    run()
