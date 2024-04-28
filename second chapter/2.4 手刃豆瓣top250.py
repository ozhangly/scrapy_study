import os
import re
import time
import requests


# 我还想着用scrapy再跑一边
url = 'http://movie.douban.com/top250'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}

pages = 10

params = {
    'start': '',
    'filter': ''
}

# 正则提取表达式
regex = re.compile(r'<li>.*?<span class="title">(?P<movie_title>\w+)</span>.*?'
                   r'<br>\n\s*(?P<movie_time>\d{4})&nbsp;'
                   r'.*?<span class="rating_num" property="v:average">(?P<rating_num>[0-9]+\.[0-9]+)</span>'
                   r'.*?<span>(?P<rating_people_num>[0-9]+[\u4e00-\u9fa5]+)</span>', re.S)

for page in range(pages):
    params['start'] = str(page*25)
    response = requests.get(url=url, headers=headers, params=params)

    # 提取内容
    page_content = response.text
    result = regex.finditer(page_content)
    print('正在提取')
    for r in result:
        movie_title = r.group("movie_title")
        movie_time = r.group("movie_time")
        movie_rating_num = r.group("rating_num")
        movie_rating_people_num = r.group("rating_people_num")

        # 如果可以的话，可以把这个保存起来
        # 进行保存等操作
        # 模拟保存操作，这里就不做了
        print(movie_title)
        print(movie_time)
        print(movie_rating_num)
        print(movie_rating_people_num)

    response.close()
    time.sleep(10)
    # print(f'第{page}次请求结束, 按任意键系统休眠10秒')
    # os.system('pause')
    # os.system('cls')
    # for sec in range(10):
    #     print(f'还剩{10-sec}秒')
    #     time.sleep(1)
    #     os.system('cls')
