# 试一试笔趣阁
# 这个网站好像有验证码来着

import aiohttp
import requests

from lxml import etree


main_url = 'https://www.beqege.cc/16747/'

# async def download_novel(url):
#     async with aiohttp.ClientSession() as session:
#
#
#
# async def main():
#     task = [
#
#     ]

if __name__ == '__main__':
    # 在主页面中请求，提取各个章节的部分是同步操作，不需要异步操作
    main_headers = {
        'authority': 'www.beqege.cc',
        'method': 'GET',
        'path': '/16747',
        'scheme': 'https',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cookie': 'islogin=1; uid=13281; uname=MaxBlack; secret=d742c10296fb8ceed6c55043dc317808; cf_clearance=JZYx1CA1ZjGTnuv6NgL_FSmdW8Hgw_82g7cU6tRIzfU-'
                  '1713665040-1.0.1.1-6fjfsX7g5uk6jZn5c_t0ND0JO42wrNC0OYVNFOLz.V7qunC6N1ShLohBVbMKpwCP.OSk1CBD9pIge4NSyb8Xlg',
        # 'If-Modified-Since': 'Sun, 08 Jan 2023 08:58:07 GMT',
        'Referer': 'https://cn.bing.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    }
    main_content = requests.get(url=main_url, headers=main_headers)
    print(main_content.text)


    # 提取main_content 的 章节id
    main_html_tree = etree.HTML(main_content.text)

    chapter_list = main_html_tree.xpath('//*[@id="list"]/dl/dd')

    for chapter in chapter_list:
        href = chapter.xpath('./a/@href')[0]
        print(href)
        break

    main_content.close()




