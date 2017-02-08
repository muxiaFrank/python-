#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/2/8 上午11:06 
"""
# 题目：输出 9*9 乘法口诀表。
for i in range(1,9):
    print
    for j in range(1,i+1):
        print "%d * %d =%d" %(i,j,i*j)