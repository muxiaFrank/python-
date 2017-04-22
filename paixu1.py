#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/4/10 下午3:59 
"""
import requests, re
import sys

reload(sys)
sys.setdefaultencoding('utf8')

str = "this is string example....wow!!!";

print "Encoded String: " + str.encode('utf-8', 'strict')

list = [1, 2, 3, 4, 5, 6]

for k in enumerate(list):
    print k
# for i, j in enumerate(list):
#     print(i, j)

# if (k) == (i, j):
#     print "yes"
print list[::-1]


def get_all_log(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            err_log = response.text.strip(' ').split('\n')
            return err_log
        else:
            raise Exception('Error Code:{0}, Error Info:{1}'.format(response.status_code, response.text))
    except Exception, e:
        print e


if __name__ == '__main__':
    url = "http://www.mocky.io/v2/58eb45f1110000651f28831c"
    # print get_all_log(url)

    str = requests.get(url)
    print str.text

    print type(str.text)

    l = str(str.text)

    group = l.match(r'test', l)

    print group

    # s = str.encode('utf-8')
    # print s
    # if s.startswith('testStep'):
    #     print s
