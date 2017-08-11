#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/8/9 下午4:34 
"""

import random
import time

from retry import retry

from retrying import retry

import os
import random


# from retrying import retry


@retry(stop_max_attempt_number=5)
def have_a_try():
    i = random.randint(0, 10)
    if i != 5:
        print i
        raise Exception("It's not 5!")
    print "It's 5!"

print have_a_try()

print 2222

#


# @retry(max_retries=2, interval=1, success=lambda x: len(x) != 0)
# def retry123():
#     l = [1, 2, 3]
#     k=[]
#
#     return l
#
#
# print retry123()



# @retry(tries=5, delay=2)
# def do_something():



#
# def retry22(times=1, exceptions=None):
#     exceptions = exceptions if exceptions is not None else Exception
#
#     def wrapper(func):
#         def wrapper(*args, **kwargs):
#             last_exception = None
#             for _ in range(times):
#                 try:
#                     return func(*args, **kwargs)
#                 except exceptions as e:
#                     last_exception = e
#             raise last_exception
#
#         return wrapper
#
#     return wrapper
#
#
# # @retry22(3)
# # def test():
# #     t = random.randint(2,6)
# #     if t != 2:
# #         print t
# #         continue
# #     else:
# #         return t
# #         break
# #
#
#
# # @retry(max_retries=6, interval=1, success=lambda x: x == 2)
# # def have_a_try():
# #     i = random.randint(0, 10)
# #     if i != 5:
# #         print i
# #         return i
# #     print "It's 5!"
# #
# # print have_a_try()
# #
# #
# # print 333333
#
# # @retry(max_retries=2, interval=1, success=lambda x: x == 2)
# # for i in range(3):
# #     x = random.randint(3)
# #
# # print x
#
#
# def take_try():
#     i = random.randint(0, 10)
#
#     return i
#
#
# def my_retry(x, fuc):
#     attempts = 0
#     success = False
#
#     while attempts < x and not success:
#         try:
#
#             if len(fuc) != 0:
#
#
#                 raise Exception(fuc)
#
#
#             success = True
#
#         except:
#             attempts += 1
#             if attempts == 3:
#                 break
#     return fuc
#
#
# fuc = []
#
# print my_retry(3, fuc)
#
# print 55555555
#
# attempts = 0
# success = False
#
# while attempts < 3 and not success:
#     try:
#         i = random.randint(1, 10)
#
#         if i != 5:
#             print i
#
#             raise Exception(i)
#         else:
#             print i,2222222222222
#
#         success = True
#
#     except:
#         attempts += 1
#         if attempts == 3:
#             break
#
# # for i in range(5):
# #     try:
# #         take_try()
# #         print take_try(), 2222
# #         break
# #     except:
# #         time.sleep(2)
