# 目标: 豆瓣
import requests

# 使用另外一种方法发送get请求
url = 'http://movie.douban.com/j/chart/top_list'

# 重新封装参数
params = {
    'type': '6',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}
# 请求数据接口
response = requests.get(url=url, headers=headers, params=params)
print(response.json())
# 爬取完数据要关掉response，如果不关的话，如果请求次数过多，那么保持的连接数过多，可能会出现请求次数过多错误
response.close()

