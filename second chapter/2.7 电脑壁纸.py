import time
import random
import requests

from bs4 import BeautifulSoup

# 比后面那个好爬多了T^T
# 这个网站看起来好正规。。。也不知道能不能成功....
# 先试一试把
# url = 'https://desk.3gbizhi.com/deskDM/index_1.html'

# 用来爬去分页的index，现在先不动，如果需要的话加个循环就可以
# index = 0

# 有史以来伪装的最全的一次
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#     'Cookie': 'wzws_sessionid=gmYwNGIwZIFkOTRhMjegZgN5eYAxMTEuMjI3LjIxMy4y; PHPSESSID=drasm23aplbqupd6sknd1k0ara; Hm_lvt_b1b08cc989f34ad5a977d00bf4c96a5a=1711503740; think_var=zh-cn; Hm_lpvt_b1b08cc989f34ad5a977d00bf4c96a5a=1711506235',
#     'Host': 'desk.3gbizhi.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
# }

# 还有一些伪装手法，比如模拟用户操作，无效点击或者滚轮之类的，这个操作需要到后面在使用，这里就先不模拟了
# response = requests.get(url=url, headers=headers)
#
# print('主页面请求成功')
#
# page_content = BeautifulSoup(response.text, 'html.parser')
#
# uls = page_content.find('div', attrs={'class': 'contlistw mtw'}).ul
#
# for li in uls.find_all('li', attrs={'class': 'box_black'}):
#     img_src = li.img['lay-src']
#     # 直接请求这个就可以
#     pause_second = random.randint(5, 10)        # 随机暂停5-10秒
#     print(f'暂停{pause_second}秒')
#     time.sleep(pause_second)
#
#     print(img_src)
#     img = requests.get(url=img_src)     # 返回的是二进制字节流，可以直接保存
#     img_name = img_src.split('/')[-1]
#     with open(file='../电脑壁纸/' + img_name, mode='wb') as fp:
#         fp.write(img.content)
#     print(img_src + '保存完毕')
#
# response.close()
