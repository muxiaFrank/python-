#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/2/11 下午5:04 
"""

def jiecheng(n):
    result = n
    for i in range(1,n):
        result *=i

    return result

number = int (input("请输入一个整数"))
result = jiecheng(number)

print ("%d阶乘是 %d" %(number,result))