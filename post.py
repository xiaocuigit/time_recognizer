# !/usr/bin/python
# encoding:utf-8

import requests
import json

if __name__ == "__main__":
    postdata = {"text": "上周周一中午12:30分张熠坐火车去的是哪里？".encode('utf-8')}
    r = requests.post('http://120.132.109.87:10088/jfycfx', data=postdata)
    print (r.text)