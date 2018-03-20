
import requests
from lxml import etree
# r = requests.get('https://www.douban.com')
# s = selector = etree.HTML(r.text)

#取出页面中所有的链接
# links = selector.xpath('//@href')
# print(type(links))
# print(links)

#抓取电影评论页

r = requests.get('https://movie.douban.com/subject/27024903/comments?status=P')
s = etree.HTML(r.text)

comments = s.xpath('//div[@class="comment"]')
for comment in comments:
    #获取用户名

    username = comment.xpath('./h3/span[2]/a/text()')[0]
    #获取评论内容
    connect = comment.xpath('./p/text()')[0]
    #获取打分星级
    stars = comment.xpath('./h3/span[2]/span[2]/@class')[0]
    comment_time = comment.xpath('./h3/span[2]/span[3]/@title')[0]
    comment_time = comment_time[0] if comment_time else ''
    print('%s  %s  %s:\n%s'%(username,stars,comment_time,connect))