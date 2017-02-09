#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/2/8 上午11:54 
"""

L=[1,2,2,2,3,3,4,4,4,4,4,5,5,5,]

for i in set(L):

    if str(L).count('%d' %(i)) > 1:
        print i

