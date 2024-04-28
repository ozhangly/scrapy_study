import re
import time

import requests


# 爬取电影详情页
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}

url = 'https://www.dyttcn.com'
# 这次请求不用带参数
response = requests.get(url=url, headers=headers, verify=False)
# 这个网站的源码的编码格式是gb2312，但是开发环境中的编码是utf8，所以会乱码，使用下面方法可以解决
# print(response.content.decode('gb2312'))
# response.close()

# 或者这种方法
# response.encoding = 'gb2312'        # gb2312 或者 gbk都可以
# print(response.text)
# response.close()

response = requests.get(url=url, headers=headers, verify=False)
response.encoding = 'gb2312'

regex = re.compile(r"最新更新.*?<ul>[\n|\s]*(?P<ul>.*?)[\n|\s]*</ul>", re.S)

results = regex.finditer(response.text)

r = next(results)
lis = r.group('ul')

li_regex = re.compile(r"<li>.*?'(?P<href>.*?)'")
li_result = li_regex.finditer(lis)

# child_regex = re.compile(r'')           # 这个正则是用来在子页面中找到下载资源的，但是页面和页面不一样，就不写了。

for li_href in li_result:
    href = li_href.group('href').strip('\n')
    child_url = '%s%s' % (url, href)
    # 然后在这里面发送请求就可以了
    with requests.get(url=child_url, headers=headers, verify=False) as response:
        response.encoding = 'gb2312'
        child_page_content = response.text

    # 获取html文档中的连接资源
    # 都一样，就不写了，就先这样了
    time.sleep(10)

response.close()
