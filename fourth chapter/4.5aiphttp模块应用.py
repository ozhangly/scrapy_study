# requests.get() 同步的代码 -> 异步的代码
# aiohttp是第三方库

import asyncio
import time

import aiohttp

# 这里先用一种简单的方法在实现
# 自己作死，找了个挺难的网站爬了，反正基本功能都实现了，现在难的就是不知道这个图片的id是怎么获取的，昨天好像看到了源码？。。。
# 也不确定要不要继续看下去....
# 大约看完了，技巧很巧妙
# 和网易云类似，也用了加密，而且不比网易的简单


# 梳理一下过程
# 1. 构造参数，这个参数是getWallPaper接口的参数
# 2. 拿到上面接口的请求后，有一个加密的字符串, 该字符串需要解密
# 3. 如何解密？    用base64先解码字符串，格式是utf8
# 4. 然后再使用ASE进行解密
# 5. 最后还要进行分割，最终才得到需要的数据

urls = [
    'https://haowallpaper.com/link/common/file/getCroppingImg/e6ba159f6bc50ba2bb6108cf17b0780d',
    'https://haowallpaper.com/link/common/file/getCroppingImg/c6fcd4e4bb7845bd0ae07fa70fb424a6',
    'https://haowallpaper.com/link/common/file/getCroppingImg/d13c5662b10a629e253521a80f1c123d'
]


async def img_download(url):
    file_name = url.rsplit('/', 1)[1]
    # session会自动关闭
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as resp:
            # resp.content.read() ====> resp.content
            # resp.text()         ====> resp.text
            # resp.json()         ====> resp.json()
            # 请求回来写入文件

            with open(file='./beautiful img/%s.png' % file_name, mode='wb') as fp:
                fp.write(await resp.content.read())         # IO操作是异步的， 需要await挂起
    # s = aiohttp.ClientSession() <===> requests.session()
    # requests.get()   //  .post()
    # s.get()          //  .post()
    # 发送请求
    # 得到图片内容
    # 保存到文件


async def main():
    tasks = [
        asyncio.create_task(img_download(url)) for url in urls
    ]

    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())
