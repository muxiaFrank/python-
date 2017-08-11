#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/6/25 下午4:25 
"""

import requests

url = "http://127.0.0.1:8080/job/aweme_API_jmeter/26/performance/"

my_content = requests.get(url).text

print  my_content

htmlfile = open('/Users/jackyoung/.jenkins/workspace/aweme_API_jmeter/output/index.html','r')

print htmlfile