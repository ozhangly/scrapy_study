import requests

from lxml import etree

url = 'http://www.zbj.com/fw/appkaifaaa'         # 猪八戒网url

count: int = 0

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}

params = {
    'k': 'APP'
}

response = requests.get(url=url, headers=headers, params=params)
response.encoding = 'utf8'

tree = etree.HTML(response.text)

service_content_div_list = tree.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div/div[2]/div[1]/div')
# //*[@id="__layout"]/div/div[3]/div/div[4]/div/div[2]/div[1]

# 然后在这个div下继续搜索
for service_content_div in service_content_div_list:
    # 要找什么呢？
    # 随便找点什么东西吗
    # 找服务的价格
    # 找服务的名字
    # 找服务企业的名字
    # 尽量做到一次访问就拿到所有数据，避免重复访问
    company_title = service_content_div.xpath('./div/a/div[2]/div[1]/div/text()')       # 自己测试了一下，这个div[2]，这个位置索引是所有子标签的索引，不是指的是第几个div
                                                                                        # 指的是这个div在所有子标签中排第2个(从1开始计数)
    servie_price  = service_content_div.xpath('./div/div[3]/div[1]/span/text()')
    servie_title  = service_content_div.xpath('./div/div[3]/div[2]/a/text()')

    print(company_title)
    print(servie_price)
    print(servie_title)

    count += 1
    if count > 10:
        break

response.close()
