#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/8/11 下午9:51 
"""

import os

print os.getcwd()


fp = open('demo_PATH.txt','w')

fp.close()


with open('demo1.txt', 'w') as f:
    print(f.read())