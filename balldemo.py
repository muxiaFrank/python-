#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/2/11 下午7:08 
"""


class ball:
    def setName(self,name):
        self.name =name
    def kick(self):
        print ("我叫 %s,该死的，谁提我") %self.name
a = ball()

print a.kick()
