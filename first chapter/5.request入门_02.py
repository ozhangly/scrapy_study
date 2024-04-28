import requests

# 请求百度翻译
url = 'https://fanyi.baidu.com/sug'
# 使用post方法发起请求

data = {
    'kw': 'cat'
}
# 发送post请求, 发送的数据放到字典中，通过data参数传递
response = requests.post(url=url, data=data)
print(response.json())    # 将服务器返回的内容直接处理成json -> dict
response.close()
