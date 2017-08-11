#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/4/26 下午8:09 
"""
a = [5, 2, 1, 9, 6]

b="asdfghjk"

for i, j in enumerate(a):
    print i, j

if b.find("sd") != -1:
    print "true"
else:
    print "false"
