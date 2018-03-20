
import urllib.request
import urllib.parse

print("GET")
params = urllib.parse.urlencode({
    'name':'xiao mi',
    'age                                                                                                                                ':2,
})
url ='http://httpbin.org/get?%s' % params

with urllib.request.urlopen(url) as f:
    print(f.read().decode('utf-8'))

print('POST')
req = urllib.request.Request('http://httpbin.org/post',
                             # data=b'a=hello&b=100',
                             data=params.encode('utf-8'),
                             method='POST')
with urllib.request.urlopen(req) as f:
    print(f.read().decode('utf-8'))
    print('f.starus = ', f.status)
    print('f.reason = ', f.reason)