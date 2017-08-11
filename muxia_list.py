#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/8/11 下午2:07 
"""

l = [{'expected': 202, 'value': 200, 'check': 'status_code', 'comparator': 'eq'}, \
     {'expected': 8, 'value': 0, 'check': 'content.status_code', 'comparator': 'eq'}]

my_content = ''

for i in l:
    if i['comparator'] == 'eq':
        my_content = my_content + "  {check} is {value}".format(check=i['check'], value=i['value'])




def err_log(l):

    my_content = ''

    for i in l:
        if i['comparator'] == 'eq':
            my_content = my_content + "\n{check} is {value}".format(check=i['check'], value=i['value'])
        elif i['comparator'] == 'len_not_eq':
            my_content = my_content + "{check} is null".format(check=i['check'])

    lll= 11111

    return 'assert false' + my_content,lll


print len(err_log(l))
