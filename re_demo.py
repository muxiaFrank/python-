#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/7/26 下午9:04 
"""
import re
import random


absolute_http_url_regexp = re.compile(r"^https?://", re.I)



i = random.randint(1,5)

print i,'+++++'


def retry11(app_type, retry=3):
    """
    重试机制，默认3次
    :param app_type: 1 >> 咚咚; 2 >> 家在; 3 >> 装修
    :param retry: 重试次数
    :return:
    """
    r1 = Retry(retry)
    if i > 0:
        print('发现diff接口，重试机制启动...')
        r1.retry1(app_type)


class Retry(object):
    def __init__(self, retry):
        """
        初始化
        :param retry:
        """
        self.retry = retry

    def retry1(self, app_type):
        """
        重试的接口类型
        1.response 响应码 非200的接口
        2.请求超时的接口
        3.其他未知情况的接口（如 代码异常导致）
        注意：已经知道失败的接口不会再重试，目前是这样考虑的
        :return:
        """
        temp = self.retry
        while self.retry > 0:
            self.retry -= 1
            # 请求接口
            print('第%d次尝试请求diff...' % (temp - self.retry,))

            # 再次求差异化文件，还有diff继续，否则停止
            if i > 0 and self.retry > 0:
                print('发现diff存在，继续尝试请求...')
                continue
            else:
                break
        print('diff机制退出...')
        # 重试机制完成，再对比一次数据，用于生成报告

def demo_retry():
    k = random.randint(1,2)




if __name__ == "__main__":

    Retry.retry1(1)