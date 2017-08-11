#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/5/14 下午2:25 
"""
import requests
from requests.exceptions import RequestException
import re, sys


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def main():
    url = sys.argv[1]
    html = get_one_page(url)
    print html


if __name__ == '__main__':
    main()
