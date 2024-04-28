import re

# 模块
# 用的不多
# result = re.findall(r'\d+', 'my phone num is 100947546')
# print(result)

# finditer: 匹配字符串中所有的内容[返回的是迭代器]， 从迭代器中拿到内容需要.group()
# it = re.finditer(r'\d+', 'my phone num is 100947546')
# for i in it:
#     print(i.group())

# search返回的结果是match对象，拿数据需要group()
# search的特点找到一个结果就返回
# result = re.search(r'\d+', 'my phone num is 10086, my mother phone is 10010')
# print(result.group())

# match 从头开始匹配, 可以认为匹配的模式是这个 ^\d+  就是必须是这个开始匹配的，如果不是那么返回结果为空None
# result = re.match(r'\d+', 'my phone num is 10086, my mother phone is 10010')
# print(result)


# 预加载正则表达式, 先加载好正则表达式，好处是可以提升一点效率，但不多，可以复用，多处使用
# obj = re.compile(r'\d+')    # 这个obj代表的这个正则表达式
# obj.search()
# obj.match()
# result = obj.finditer('my phone num is 10086, my mother phone is 10010')
# for r in result:
#     print(r.group())

# 比较重要的一个
# s = "<div class='red_box'><span id='1'>红色盒子</span></div>" \
#     "<div class='yellow_box'><span id='2'>黄色盒子</span></div>" \
#     "<div class='green_box'><span id='3'>绿色盒子</span></div>" \
#     "<div class='blue_box'><span id='4'>蓝色盒子</span></div>"

# (?P<分组名字>正则)  可以单独从正则匹配的内容中进一步提取内容
# reg = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<span_content>.*?)</span></div>", re.S) # re.S 作用是.能匹配换行符
#
# print(s)
# results = reg.finditer(s)
# for res in results:
#     print(res.group("span_content"))
#     print(res.group("id"))

s = '<span class="title">末代皇帝</span>'
regex = re.compile(r'<span class="title">(?P<movie_title>\w+)</span>')

result = regex.finditer(s)
for r in result:
    print(r.group('movie_title'))

