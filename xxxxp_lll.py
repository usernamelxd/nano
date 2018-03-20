import requests
from lxml import etree

#
# r = requests.get('https://movie.douban.com/')
#
# s = selector = etree.HTML(r.text)
#
# links = s.xpath('//@href')
# print(type(links),len(links))
# print(links)
for i in range(2,9):
    print(i)

    r = requests.get('https://www.amazon.cn/%E4%BA%BA%E9%97%B4%E8%AF%8D%E8%AF%9D-%E7%8E%8B%E5%9B%BD%E7%BB%B4/product-reviews/B01DVYESFY/ref=cm_cr_getr_d_paging_btm_next_'+str(i)+'?ie=UTF8&reviewerType=all_reviews&pageNumber='+str(i)+'')
    s = etree.HTML(r.text)

    comments = s.xpath('//*[@class="a-section celwidget"]')

    for comment in comments:
        #获取用户名

        #//*[@class="a-section review-views celwidget"]/div[1]/div/div[1]/a/div[2]
        username = comment.xpath('./div[2]/span[1]/a/text()')
        #获取评论内容
        connect = comment.xpath('./div[4]/span/text()')
        #获取打分星级
        stars = comment.xpath('./div[1]/a[1]/i/span/text()')
        comment_time = comment.xpath('./div[2]/span[3]/text()')
        comment_time,username,connect,stars = comment_time[0],username[0],connect[0],stars[0] if comment_time else ''

        print('%s %s -- %s -- %s'%(username,stars,connect,comment_time))
        # print(connect)
        # print(type(stars))







