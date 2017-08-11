#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: Muxia
@time: 2017/2/7 下午9:05
"""

import re, requests

# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if( i != k ) and (i != j) and (j != k):
#                 print i,j,k

# list1 = ['key1','key2','key3']
# list2 = ['1','2','3']
# print dict(zip(list1,list2))
#
#
# list3=['http://aweme.snssdk.com/aweme/v1/commit/challenge/', 'https://aweme.snssdk.com/aweme/v1/comment/list/']
#
# print len(list3)
sample_dic = {'a': 'hi', 'b': 'there'}

for key, value in sample_dic.items():
    my_str = "%s:%s" % (key, value)
    print my_str

# list1 = [1,2,3,4,5]
# list2 = [4,5,6,7,8]
# print [l for l in list1 if l in list2]

url = "http://ci.byted.org/view/aweme/job/aweme_server_online_vip/9924/console"

response = requests.get(url)

err_log = unicode(response.text)

print err_log

print type(err_log),"11111111"

my_content = re.findall(r'ASSERTION FAILED -&gt;(.*?)\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d,\d\d\dERROR(.*?)测试用例说明', err_log, re.S)

print my_content
# print len(set(my_content))

# my_test = """19:55:41,698 ERROR [SoapUITestCaseRunner] ASSERTION FAILED -> assert Root.music_list.size() !=0
#        |    |          |      |
#        |    []         0      false
#        [extra:[now:1495886141640], has_more:0, status_code:0, cursor:30, msg:success, music_list:[]]
# 19:55:41,698 ERROR [SoapUITestCaseRunner] REST Request failed, exporting to [/home/ci_slave/jenkins/workspace/aweme_server_online/log/aweme-歌单界面_hot_list-REST_Request-0-FAILED.txt]
# # c="""
#
# print type(my_test),"22222222"
#
# my_code = re.findall(r'ASSERTION FAILED ->(.*?)\d\d:\d\d:\d\d,\d\d\d ERROR',my_test,re.S)
#
# print my_code

# herf=sdsdaherf=sadasdada+++
#   sdad123,21312!!!"""
#
# print c
#
# a=re.findall(r'herf=(.*?)', c,re.S)
#
# print a

sid = {"sessionid": "386746662dc25d42fcf0dc8ca4178880"}

my_post = requests.get(
        "http://aweme.snssdk.com/aweme/v1/music/collect/?iid=12589712737&ac=WIFI&os_api=18&app_name=aweme&channel=test&idfa=00000000-0000-0000-0000-000000000000&device_platform=iphone&build_number=15107&vid=CE961EBD-B47C-4267-AFA8-50D4AC100376&openudid=f2ab25a7bae7cb5f57273023f3c2f1b74eb09b76&device_type=iPhone8,1&app_version=1.5.1&device_id=35515683046&version_code=1.5.1&os_version=10.2.1&screen_width=750&aid=1128&count=20&max_time=1500984970&user_id=52234155317&cp=3c849857ab757262e1&as=a1058307eaf8f90677&ts=1500984970 HTTP/1.1",
        cookies=sid
    )

print my_post.text

print "11111"
