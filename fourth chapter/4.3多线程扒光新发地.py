# 1. 如何提取单个页面上的数据
# 2. 上线程池，多个页面同时抓取
import requests

from lxml import etree
from concurrent.futures import ThreadPoolExecutor

headers = {
    'User-Agent': ''
}


# 提却的结果怎么保存，有时候需要id，所以这里也将id传过来了
def down_one_page(url, id):
    # 这种写法是在网站没改版之前的写法，改版之后的直接请求数据接口就可以获取了
    # 如果实在想爬取什么东西，可以试试豆瓣的top250
    one_page_resp = requests.get(url, headers=headers)
    tree = etree.HTML(one_page_resp.text)

    table = tree.xpath('/html/xxxx/table')[0]
    trs = table.xpath('./tr[position() > 1]')  # 新学到的，这个是置大于1的tr(在xpath中位置是从1开始取位计数的)
    for tr in trs:
        # 这样再进行遍历就可以了
        # 去提取东西
        tr.xpath('./text()')
        # 在进行保存就可以了


if __name__ == '__main__':
    # 当请求的很多时，单线程效率会很低，所以使用多线程
    # 但是还有一点就是线程的个数和调度不好控制，所以使用线程池来自动进行调度
    base_url = ''
    with ThreadPoolExecutor(8) as tp:
        for i in range(1, 1000):
            url = base_url + '/%d.html' % i
            tp.submit(down_one_page, url=url, id=i)

    print('全部提取完毕')
