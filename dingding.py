#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/8/11 下午3:16 
"""

#code from www.361way.com
#coding: utf-8
import json,urllib2


def send_dingding(l):

    url = "https://oapi.dingtalk.com/robot/send?access_token=8cbd675cf35107d669743e31ab41d412dbbf82d3b0119e9a6cd86406acc875b5"
    header = {
        "Content-Type": "application/json",
        "charset": "utf-8"
    }
    data = {
         "msgtype": "text",
            "text": {
                "content": l
            },
         "at": {
                "isAtAll":False  # at为非必须
             }
        }
    sendData = json.dumps(data)
    request = urllib2.Request(url,data = sendData,headers = header)
    urlopen = urllib2.urlopen(request)

print send_dingding(123)