#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/2/11 下午5:13 
"""
def jiecheng(n):
    if n ==1 :
        return 1
    else:
        return n*jiecheng(n-1)

number = int(input("请输入一个整数："))

result =jiecheng(number)

print "%d 的阶乘是 %d" %(number,result)