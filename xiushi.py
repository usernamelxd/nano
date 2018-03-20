import requests
from lxml import etree

r = requests.get('https://www.qiushibaike.com/text/')
s = etree.HTML(r.text)
comments = s.xpath('//div[@class="col1"]')
for comment in comments:

    #获取用户名
    username = comment.xpath('./div/div[1]/a[2]/h2/text()')

    #获取评论内容
    connect = comment.xpath('./div/a/div/span/text()')

    for i in range(len(username)):
        print(username[i],connect[i])
    # print('%s:%s'%(username,connect))
