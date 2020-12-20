# -*- coding:utf-8 -*-

import re


def captcha(string):
    pattern = r'[a-zA-Z0-9]{4,}'
    return re.findall(pattern, string)


if __name__ == '__main__':
    result = captcha('515sa')
    print(result)
