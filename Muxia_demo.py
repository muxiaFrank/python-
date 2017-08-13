#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/8/13 下午5:01 
"""

import  argparse


""" parse command line options and run commands.
"""

def main():
    parser = argparse.ArgumentParser(
        description='AAA.')

    parser.add_argument(
        '-V', '--version', dest='version', action='store_true',
        help="show version")


    t = "hello world !"


    return  t

