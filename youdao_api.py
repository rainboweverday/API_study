#/usr/bin/env python
#coding=utf-8

import httplib2
import hashlib
import urllib
import random
import json


appKey = 'xxx'
secretKey = 'xxx'

httpClient = None
myurl = '/api'
q = 'good'
fromLang = 'EN'
toLang = 'zh-CHS'
salt = random.randint(1, 65536)

sign = appKey + q + str(salt) + secretKey
sign = sign.encode('utf-8')
m1 = hashlib.md5()
m1.update(sign)
sign = m1.hexdigest()
myurl = myurl + '?appKey=' + appKey + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt='+ str(salt) + '&sign=' + sign

try:
    httpClient = httplib2.HTTPConnectionWithTimeout('openapi.youdao.com')
    httpClient.request('GET', myurl)

    response = httpClient.getresponse()
    response_data = response.read()
    response_data = response_data.decode('utf-8')
    response_data = json.loads(response_data)
    # print(response_data)
    # print(type(response_data))
    for k in response_data:
        print(k, ':', response_data[k])

except Exception as e:
    print(e)
finally:
    if httpClient:
        httpClient.close()
