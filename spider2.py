#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/5/15 下午9:02 
"""

from bs4 import BeautifulSoup
import requests,re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""


url = 'http://ci.byted.org/view/aweme/job/aweme_server_online_vip/8337/console'

url2 = "https://aweme.snssdk.com/aweme/v1/feed/"

html1 = requests.get(url).text

html2 = requests.get(url2).text

unicodehtml = html.decode("utf-8")

unicodehtml1 = html1.decode("utf-8")

unicodehtml2 = html2.decode("utf-8")


myitems = re.findall(r"<a href=(.*?) class=(.*?)</a>",unicodehtml)

items = []

for item in myitems:
    items.append(item[0])

print items,len(items)

myitems2 = re.findall(r'"aweme_id":(.*?),',unicodehtml2)

print list(set(myitems2))

err_html = str(html1.split('\n'))

if re.findall("Properties",html1):
    myviews = re.findall(r'Messages\s+--+(.*?)--+\s+Properties',err_html,re.S)
    my_code = re.findall(r'Properties\s+--+(.*?)Method:',err_html,re.S)
    err_api = re.findall(r"<URL: a href=(.*?)--+\s+Request", err_html, re.S)
    print err_api
    print myviews,len(myviews)
    print my_code
else:
    print "未找到"

# soup = BeautifulSoup(html1,'lxml')
#
# print soup.find_all(string=re.compile("--+\s+Properties\s+--+$"))

# strvar = """"
# 1111
# hello
# world!
# 2222"""
#
#
#
# pat = re.findall(r"111(.*?)222", strvar,re.S)
# print pat