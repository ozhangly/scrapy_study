import requests

url = 'http://www.baidu.com/s?wd=神里绫华'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
}

# 嘛。。这也算学到新东西了。。就是
# 所有在地址栏输入的网址的请求方式都是get方法的请求
response = requests.get(url=url, headers=headers)
with open(file='./requests module.html', mode='w', encoding='utf8') as fp:
    fp.write(response.content.decode('utf8'))
response.close()
print('over')
