#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/2/28 下午6:36 
"""

import sys

print "脚本名" ,sys.argv[0]
for i in range(1,len(sys.argv)):
    print "参数",i,sys.argv[i]
