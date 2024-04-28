from urllib.request import urlopen

url = "http://www.baidu.com"
response = urlopen(url)
# 响应
# response.read() 返回的字节流，需要decode转成想要的编码成想要的文件
# print(response.read().decode('utf8'))
with open(file='./first_bug_baidu.html', mode='w', encoding='utf8') as f:
    f.write(response.read().decode('utf8'))     # 读取到的网页源代码
print('over')
