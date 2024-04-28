import requests
from bs4 import BeautifulSoup

# Beautifulsoup感觉不太好用
# 原本想用beautifulsoup4来提取网页的，但是现在这个网站改成了前后端分离的方式，只能通过post接口请求数据了
# 但是也简单不少~~
# url = 'http://www.xinfadi.com.cn/getPriceData.html'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
# }
#
# data = {
#     'limit': '',
#     'current': '',
#     'pubDateStartTime': '',
#     'pubDateEndTime': '',
#     'prodPcatid': '1187',
#     'prodCatid': '',
#     'prodName': ''
# }
#
# with requests.post(url=url, headers=headers, data=data) as response:
#     fruit_data = response.json()
#     print(fruit_data)
# 然后简单筛选下保存就可以

###########################################################
# 还是简单的记一下BeautifulSoup的使用方式
# 下面这段代码不可以直接执行！！！！
# 这个网站已经更换架构了！！！
# response = requests.get(url=url, headers=headers)       # 响应
# 1. 把页面交给BeautifulSoup进行处理生成bs对象
# page = BeautifulSoup(response.text, 'html.parser')      # 指定html解析器，因为BeautifulSoup不能自己判断传的文本一定是html，需要指定解析器
# 2. 从bs对象中查找数据
# find(标签, 属性=值)
# find_all(标签, 属性=值)
# table = page.find('table', class_='XXX')                # class是python的关键字, 这种方法查找的是class=XXX的table标签
# 或者也可以这么用：
# table = page.find('table', attrs={'class': 'XXX'})      # 个人认为这种方法更好用
# print(table)


# 使用 beautifulsoup 爬一爬电影天堂

# url = 'https://www.dyttcn.com'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
# }
#
# with requests.get(url=url, headers=headers, verify=False) as response:
#     response.encoding = 'gb2312'
#     content_page = BeautifulSoup(response.text, 'html.parser')
#
# div = content_page.find('div', attrs={'class': 'co_content222'})
#
# hrefs = []
# lis = div.find_all('li')
# for li in lis:
#     hrefs.append(li.a['href'])
#
# # 已经找到了，然后再去发送请求就可以了, 下面就不写了
# print(hrefs)
