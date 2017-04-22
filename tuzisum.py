#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/2/11 下午5:37 
"""


def fab(n):

    if n < 1:
        print "数据有误"
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1) + fab(n-2)

result = fab(20)

if result != -1:
    print ("总共有兔子 %d 只" %result)