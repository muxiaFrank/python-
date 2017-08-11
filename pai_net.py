#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/5/13 下午8:13 
"""
from bs4 import BeautifulSoup
import re, requests

url1 = "http://ci.byted.org/view/aweme/job/aweme_iOS_inhouse_branch1/112/"

url2 = "https://www.baidu.com"

html_sample = requests.get(url1).text

print requests.get(url1).json

#err_api = re.findall(r'"max_cursor":(.*?),',html_sample,re.S)

#print str(err_api).replace('u\'','\'')

print html_sample

# print html_sample
#
# print type(html_sample)
# arr = []
# for i in html_sample["aweme_list"]:
#
#
#     arr.append(i["share_url"])
#
#
# print arr

# print html_sample
#
# soup = BeautifulSoup(html_sample,"html_sample")
#
# print soup.select("div")

def get_parameters(PATH):
    with open(PATH, 'rb') as f:
        data = [ln.strip() for ln in f]

    return '/'.join(list(data))

a = lambda get_parameters(PATH):(with open(PATH, 'rb') as f:data = [ln.strip() for ln in f]

