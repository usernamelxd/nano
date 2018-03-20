import threading
import redis
import signal
import time
from queue import Queue
import requests
from lxml import etree
#入口页面地址
start_url = 'http://www.qianmu.org/2018USNEWS%E4%B8%96%E7%95%8C%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D'
#待抓取页面地址
# link_queue =Queue()
DOWNLOAD_NUM = 10
#下载延迟
DOWNLOAD_DELAY = 0.1
#线程池
threads = []

download_pages = 0

r = redis.Redis(password='sunck')

thread_on = True

def fetch(url):
    #执行页面抓取
    global download_pages
    r = requests.get(url)
    download_pages += 1
    #返回抓取页面内容，并去除页面的制表符
    return r.text.replace('\t','')

def parse(html):
    #解析入口页面
    dom = etree.HTML(html)
    #获取页面中的表格每一行的第二列的超链接
    links = dom.xpath('//div[@id="content"]/table/tbody/tr/td[2]/a/@href')
    #把这些链接放入待抓取队列中

    for link in links:
        # 如果有不规则链接，则补全
        if not link.startswith('http://'):
            link = 'http://www.qianmu.org/%s' % link
            #将链接放入下载队列
        # link_queue.put(link)
        if r.sadd('qianmu.seen',link):
            r.rpush('qianmu.queue',link)

def parse_university(html):
    """解析大学详情页面"""

    dom = etree.HTML(html)
    #先选择出表格的父节点，以减少重复代码
    infobox = dom.xpath('//div[@id="wikiContent"]/div[@class="infobox"]')[0]
    # 选择出表格中的额每一行的第一列中的文本
    keys = infobox.xpath('./table/tbody/tr/td[1]//text()')
    # 选择出表格中的额每一行的第二列的节点
    cols = infobox.xpath('./table/tbody/tr/td[2]')
    # 遍历第二列的节点，并提取出每一个单元格的文本
    values = [','.join(col.xpath('.//text()')) for col in cols]
    # 最后，讲第一列和第二列中的数据合并成一个字典，组成该大学的信息
    info = dict(zip(keys, values))
    r.lpush('qianmu.items',info)


def downloader(i):
    while thread_on:
        #从队列中读取一个链接，如果没有，则阻塞
        # link = link_queue.get()
        link = r.lpop('qianmu.queue')
        if link :
            parse_university(fetch(link))
        print('remaining queue: %s' %r.llen('qianmu.queue'))
        time.sleep(DOWNLOAD_DELAY)
    print('Thread-%s exit now' % i)

def signal_handler(signum,frame):
    print('received CTRL+C,wait for exit grancefully.....')
    global thread_on
    thread_on = False



if __name__ == '__main__':
    start_time = time.time()
    #抓取并处理入口页面，提取首页内的大学页面链接
    parse(fetch(start_url))

    for i in range(DOWNLOAD_NUM):
        t = threading.Thread(target=downloader,args=(i+1,))
        t.start()
        threads.append(t)
        print('Thread-%s start **'%t.name)



    signal.signal(signal.SIGINT,signal_handler)


    #退出线程
    for t in threads:
        t.join()
    #计算程序消耗时间
    print('download %s pages in %.2f seconds' % (download_pages,time.time()-start_time))