
import requests
params = {

    'name':'Daming',
    'age':20,
}

print('GET请求')
r = requests.get('http://httpbin.org/get',
                 params = params,
                 headers = {
                     'User-Agent':'XXXX',
                     'Referer':'http://httpbin.org',
                 })
print(r.text)


print('POST请求')
r = requests.post('http://httpbin.org/post',
                  data = params)
print(r.json())






print('dai cookie qingqiu')
cookies = {'sessionid': '1234', 'token': 'xxxx'}
r = requests.get('http://httpbin.org/cookies',cookies=cookies)
print(r.text)






print('绘画保持')
s = requests.Session()
params = {
    'userid':'1234',
    'token':'fafasfsdfdsgdfdfgdfgdgsdfs'
}
#先用 session对象请求另一个url，该url会返回两个cookies
s.get('http://httpbin.org/cookies/set',params=params)
#再用session 对象请求另一个url 会将刚才返回的cookies床上去
r = s.get('http://httpbin.org/cookies')
print(r.text)






print('抛出异常')
ok_r = requests.get('http://httpbin.org/status/200')
print(ok_r.status_code)
#当http code 为200时  不会抛出异常
ok_r.raise_for_status()

bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
#当 http code 部位200时，抛出异常
bad_r.raise_for_status()
