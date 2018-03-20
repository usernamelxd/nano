import urllib
from urllib import request
import requests


def first():
    #最基本的
    url = "http://www.baidu.com/"
    resp = urllib.request.urlopen(url)
    #页面源码
    print (resp.read())
    #返回的头信息
    print (resp.info())
    #返回的http状态码
    print (resp.status)
    #响应的url
    print (resp.geturl())
if __name__=="__main__":
    first()

