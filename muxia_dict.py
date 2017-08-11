#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/8/11 下午4:20 
"""

import os
import  random
# my_dict = {'request': {'url': '/aweme/v1/find/?iid=13270500294&ac=WIFI&os_api=18&app_name=aweme&channel=test&idfa=CADE4A2B-D6B4-42DF-B9B9-0438721DFDC0&device_platform=iphone&build_number=15207&vid=DA6B9DE0-EE58-4B27-B1A7-6E8788388442&openudid=deaab76b3a35945d86758f5380ce8e5f98628d4e&device_type=iPhone8,1&app_version=1.5.2&device_id=36999832878&version_code=1.5.2&os_version=9.3.2&screen_width=750&aid=1128&cp=68ed94515f9d8b50e1&as=a1b5c6e8c56ed9c539&ts=1502176741', 'headers': {'Api_test': 'Api_test', 'User-Agent': 'AwemeInhouse/1.5.2 (iPhone; iOS 9.3; Scale/2.00)'}, 'cookies': None, 'method': 'GET'}, 'name': '006_aweme_find.banner', 'validators': [{'expected': 200, 'value': 200, 'check': 'status_code', 'comparator': 'eq'}, {'expected': 0, 'value': 0, 'check': 'content.status_code', 'comparator': 'eq'}, {'expected': 1, 'value': [{u'banner_url': {u'url_list': [u'https://p3.pstatp.com/obj/34b200058d06e1753bea', u'https://pb9.pstatp.com/obj/34b200058d06e1753bea', u'https://pb3.pstatp.com/obj/34b200058d06e1753bea'], u'uri': u'34b200058d06e1753bea'}, u'title': u'\u9b42\u6597\u7f57', u'bid': u'522', u'height': 518, u'width': 1080, u'schema': u'aweme://challenge/detail/1575056258962445'}, {u'banner_url': {u'url_list': [u'https://p3.pstatp.com/obj/30ee000522aff52a4c6d', u'https://pb9.pstatp.com/obj/30ee000522aff52a4c6d', u'https://pb3.pstatp.com/obj/30ee000522aff52a4c6d'], u'uri': u'30ee000522aff52a4c6d'}, u'title': u'\u8fb0\u4ea6\u5112', u'bid': u'518', u'height': 518, u'width': 1080, u'schema': u'aweme://challenge/detail/1574163149144077'}, {u'banner_url': {u'url_list': [u'https://p9.pstatp.com/obj/30ed000c8c1f4cec17f3', u'https://pb1.pstatp.com/obj/30ed000c8c1f4cec17f3', u'https://pb3.pstatp.com/obj/30ed000c8c1f4cec17f3'], u'uri': u'30ed000c8c1f4cec17f3'}, u'title': u'\u6211\u4e5f\u662f\u6b4c\u624b', u'bid': u'516', u'height': 518, u'width': 1080, u'schema': u'aweme://challenge/detail/1574787982418013'}, {u'banner_url': {u'url_list': [u'https://p3.pstatp.com/obj/30ef0006b8d34ac526ca', u'https://pb9.pstatp.com/obj/30ef0006b8d34ac526ca', u'https://pb3.pstatp.com/obj/30ef0006b8d34ac526ca'], u'uri': u'30ef0006b8d34ac526ca'}, u'title': u'transition', u'bid': u'501', u'height': 518, u'width': 1080, u'schema': u'https://aweme.snssdk.com/magic/runtime/?id=343'}, {u'banner_url': {u'url_list': [u'https://p1.pstatp.com/obj/30ef0004b6e7640a1931', u'https://pb3.pstatp.com/obj/30ef0004b6e7640a1931', u'https://pb3.pstatp.com/obj/30ef0004b6e7640a1931'], u'uri': u'30ef0004b6e7640a1931'}, u'title': u'\u6296\u97f3\u62cd\u6444\u6307\u5357', u'bid': u'496', u'height': 518, u'width': 1080, u'schema': u'aweme://challenge/detail/1568518039001089'}, {u'banner_url': {u'url_list': [u'https://p1.pstatp.com/obj/216900178e81d032fe6e', u'https://pb3.pstatp.com/obj/216900178e81d032fe6e', u'https://pb3.pstatp.com/obj/216900178e81d032fe6e'], u'uri': u'216900178e81d032fe6e'}, u'title': u'\u5165\u5751\u5fc5\u8bfb', u'bid': u'249', u'height': 518, u'width': 1080, u'schema': u'https://www.amemv.com/aweme/in_app/activity/pic/?img=bg1_821cd10019c6174fc4ce12425b17cfc5,bg2_0bd25a2a6b750009894a204d80e8e050&format=png'}], 'check': 'content.banner', 'comparator': 'len_not_eq'}]}
#
#
# print my_dict['name']
import logging

l= '123'

m = [].append(l)

print m

# with open("/Users/jackyoung/Documents/ApiTestEngine/testcase/demo.txt", 'r+')  as f:
#     f.truncate()
#
# for i in range(1,5):
#     x = random.randint(1, 5)
#     with open("/Users/jackyoung/Documents/ApiTestEngine/testcase/demo.txt", 'a')  as f:
#
#         f.write(str(x)+'\n')

def get_parameters(PATH):
    with open(PATH, 'r') as f:
        data = [ln.strip('\r') for ln in f]

    errorlog_list = list(set(data))

    errorlogs = ''

    for i in errorlog_list:
        errorlogs =  errorlogs + i

    my_error = "A total of {times} failures".format(times=len(errorlog_list))+'\n'+errorlogs

    return my_error








t = get_parameters('/Users/jackyoung/Documents/ApiTestEngine/testcase/demo.txt')


# fp = open('/Users/jackyoung/Documents/ApiTestEngine/testcase/demo1.txt','w')
#
# fp.close()

# if os.path.isfile('/Users/jackyoung/Documents/ApiTestEngine/testcase/demo1.txt'):
#     os.remove('/Users/jackyoung/Documents/ApiTestEngine/testcase/demo1.txt')
# else:
#
#     pass


l1 = ['b','c','d','b','c','a','a']
l2 = list(set(l1))

print l2


print t

# errorlog_list = list(set(t))
#
# print errorlog_list
#
# print len(set(t))
#
# errorlogs = ''
# for i in errorlog_list:
#
#     errorlogs = '\n'+errorlogs+i
#
# print errorlogs



