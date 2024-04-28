# 从主页面抓取全部5个页面
import re
import time
import random
import requests

from lxml import etree

main_url = 'https://www.pearvideo.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
}

main_response = requests.get(url=main_url, headers=headers)

print('主页面请求成功')
main_tree = etree.HTML(main_response.text)
print('正在提取主页面内容')

lis = main_tree.xpath('//*[@id="actwapSlideList"]/li')
for li in lis:
    # 拿到li下面的a的href
    child_url = li.xpath('./a/@href')[0]
    print('提取子页面url')
    # 构造访问videoStatus的参数
    cont_id = re.findall(r'\d+', child_url)[0]
    mrd = '%.16f' % random.random()

    child_url_referer = main_url + child_url
    child_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        'Referer': child_url_referer
    }
    # videoStatus
    video_status_url = 'https://www.pearvideo.com/videoStatus.jsp'
    video_status_param = {
        'contId': cont_id,
        'mrd': mrd
    }

    sleep_time = random.random() * 10 + 5
    time.sleep(sleep_time)

    print('请求视频参数')
    video_status = requests.get(url=video_status_url, headers=child_headers, params=video_status_param)

    video_status = video_status.json()
    print('提取视频url')
    video_url = video_status['videoInfo']['videos']['srcUrl']

    # 需要把video_url替换一下
    video_url = re.sub(r'/\d+-', '/cont-%s-' % cont_id, video_url)

    print('请求视频')
    video_content = requests.get(url=video_url)

    print('正在下载视频')
    with open(file='./pearVideo/%s.mp4' % cont_id, mode='wb') as fp:
        fp.write(video_content.content)


