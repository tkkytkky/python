#-*- coding: utf-8 -*-

import requests

param = {'hl' : 'ja'}
url = "https://www.google.com/"
r = requests.get(url, params=param)
#r = requests.get("https://www.google.com/")
#r = requests.get("http://example.com")




print("print(r)=",r)
print("print(r.url)=",r.url)
print("print(r.headers)=",r.headers)

