import asyncio
import re
import requests
import aiohttp
import aiofiles


# page_url = 'https://kanjuwang.co/kjpp/134308-1-1.html'
#
#
# # 需要再提取其中的m3u8的url
# response = requests.get(url=page_url, headers={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
# })
#
# print(response.text)
#
# result = re.search(r'},"url":"(?P<url>.*?)",', response.text, re.S)
# m3u8_url = result.group('url')
# m3u8_url = re.sub(r'\\', '', m3u8_url)      # 替换掉url中的\字符
#
# # 访问这个url
# m3u8_resp = requests.get(url=m3u8_url, headers={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
# })
#
# with open(file='./video/更衣人偶.m3u8', mode='wb') as fp:
#     fp.write(m3u8_resp.content)
#
# m3u8_resp.close()
#
# response.close()

m3u8_url = 'https://sd7.taopianplay1.com:43333/c56b1bc09da3/HD/2023-03-24/30/e37ffd316110/8083f584f660/playlist.m3u8'

base_ts_url = m3u8_url.rsplit('/', maxsplit=1)[0]
print(base_ts_url)


async def download_m3u8_content(url):
    ts_id = url.rsplit('/', maxsplit=1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
        }) as resp:
            async with aiofiles.open(file=f'./video/{ts_id}', mode='wb') as fp:
                await fp.write(await resp.content.read())


async def main(url_list):
    tasks = [
        asyncio.create_task(download_m3u8_content(url)) for url in url_list
    ]
    await asyncio.wait(tasks)


if __name__ == '__main__':

    url_list = []
    with open(file='./video/更衣人偶.m3u8', mode='r') as fp:
        for lines in fp.readlines():
            if lines.find('#') == -1:
                # 拼接字符串
                ts_url = base_ts_url + '/' + lines.strip()
                # 发送请求
                url_list.append(ts_url)

    asyncio.run(main(url_list))


