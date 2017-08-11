#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2017/5/3 下午5:49 
"""

import requests, pprint, re
import json
from bs4 import BeautifulSoup

#
# d_url = requests.get(
#     "https://api.amemv.com/aweme/v1/feed/?os_api=18&app_name=aweme&channel=test&idfa=00000000-0000-0000-0000-000000000000&device_platform=iphone&app_version=1.4.1&vid=A83FDE96-D4CD-4592-96B6-1DB0B333A09F&openudid=531503afdd1677014742e830e99c16effb0fca38&device_type=iPhone8,2&version_code=1.4.1&os_version=10.3.1&screen_width=1242&aid=1128&ac=WIFI&count=6&min_cursor=1493795984205&type=0&user_id=54012025324&cp=94339e53a39905bde1&as=a1b599b01ac3891bf9")
# d_rep = BeautifulSoup(d_url.text.encode("utf8"), "html.parser")
#
# print d_rep
#
#
# element = d_rep.find_all(id="aweme_id")
#
# print element

# myresponse = d_url.json()
# pprint.pprint(myresponse)

# re_sult = re.findall("u'aweme_id'",myresponse)
# print re_sult

# arr = []
# for m in myresponse['aweme_list']:
#     # print m['aweme_id']
#     arr.append(m['aweme_id'])
#
# print arr

# mycookie = {"sessionid": "d277c7a3e5f20f165711555087d95df5"}
#
# my_post = requests.get(
#     "https://api.amemv.com/aweme/v1/aweme/post/?iid=10373571871&ac=WIFI&os_api=18&app_name=aweme&channel=test&idfa=7383813F-05BF-42EE-97C8-5727DDC4120A&device_platform=iphone&build_number=14200&vid=4D10CF18-F220-45B6-B913-AF5B24F31FB2&openudid=88e25b736f9770e27001b05babfc1297d27b6832&device_type=iPhone8,4&app_version=1.4.2&device_id=36204918782&version_code=1.4.2&os_version=9.3&screen_width=640&aid=1128&count=21&max_cursor=0&min_cursor=0&user_id=52234155317&cp=a690915300e91a0fe1&as=a1056a21e08969808e",
#     cookies=mycookie
# )
#
# my_poet_response = my_post.json()
#
# # print my_poet_response
#
# arr1 = []
#
# for i in my_poet_response['aweme_list']:
#     arr1.append(i['aweme_id'])

sid = {"sessionid": "13c8b9347b4f5a29b9525a3f94f94929"}


def my_video(sid):
    my_post = requests.get(
        "https://api.amemv.com/aweme/v1/aweme/post/?iid=10373571871&ac=WIFI&os_api=18&app_name=aweme&channel=test&idfa=7383813F-05BF-42EE-97C8-5727DDC4120A&device_platform=iphone&build_number=14200&vid=4D10CF18-F220-45B6-B913-AF5B24F31FB2&openudid=88e25b736f9770e27001b05babfc1297d27b6832&device_type=iPhone8,4&app_version=1.4.2&device_id=36204918782&version_code=1.4.2&os_version=9.3&screen_width=640&aid=1128&count=21&max_cursor=0&min_cursor=0&user_id=52234155317&cp=a690915300e91a0fe1&as=a1056a21e08969808e",
        cookies=sid
    )

    my_post_response = my_post.json()

    vid = []

    for i in my_post_response['aweme_list']:
        vid.append(i['aweme_id'])

    return vid


print my_video(sid)


# for m in arr1:
#     del_cookies = {"sessionid": "d277c7a3e5f20f165711555087d95df5"}
#     del_body = {"aweme_id":m}
#
#     r = requests.post(
#         "https://api.amemv.com/aweme/v1/aweme/delete/?os_api=18&app_name=aweme&channel=test&idfa=00000000-0000-0000-0000-000000000000&device_platform=iphone&app_version=1.4.1&vid=FA74DFBB-D83B-4C65-AE02-549C973B42DA&openudid=f2ab25a7bae7cb5f57273023f3c2f1b74eb09b76&device_type=iPhone8,1&version_code=1.4.1&os_version=10.2.1&screen_width=750&aid=1128&ac=WIFI&cp=94ba98593b980763e1&as=a18529c093fbe906e9"
#     ,cookies = del_cookies,data=del_body
#     )

# r = requests.post(
#     "https://api.amemv.com/aweme/v1/aweme/delete/?os_api=18&app_name=aweme&channel=test&idfa=00000000-0000-0000-0000-000000000000&device_platform=iphone&app_version=1.4.1&vid=FA74DFBB-D83B-4C65-AE02-549C973B42DA&openudid=f2ab25a7bae7cb5f57273023f3c2f1b74eb09b76&device_type=iPhone8,1&version_code=1.4.1&os_version=10.2.1&screen_width=750&aid=1128&ac=WIFI&cp=94ba98593b980763e1&as=a18529c093fbe906e9"
#     , cookies= mycookie,data=)
# print r.text

def delete_myvideo(vid):
    for m in vid:
        del_body = {"aweme_id": m}

        r = requests.post(
            "https://api.amemv.com/aweme/v1/aweme/delete/?os_api=18&app_name=aweme&channel=test&idfa=00000000-0000-0000-0000-000000000000&device_platform=iphone&app_version=1.4.1&vid=FA74DFBB-D83B-4C65-AE02-549C973B42DA&openudid=f2ab25a7bae7cb5f57273023f3c2f1b74eb09b76&device_type=iPhone8,1&version_code=1.4.1&os_version=10.2.1&screen_width=750&aid=1128&ac=WIFI&cp=94ba98593b980763e1&as=a18529c093fbe906e9"
            , cookies=sid, data=del_body
        )


while len(my_video(sid)) != 0:
    delete_myvideo(my_video(sid))
else:
    pass
