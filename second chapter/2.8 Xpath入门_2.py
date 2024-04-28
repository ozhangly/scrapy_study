from lxml import etree

# xpath是神！！！
tree = etree.parse('./sample_xpath.html')

# result = tree.xpath('/html')
# result = tree.xpath('/html/body/ul/li/a/text()')                  # []
# result = tree.xpath('/html/body/ul/li[1]/a/text()')               # ['百度'] xpath 的顺序是从1开始数的, []表示索引
# result = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")   # ['大炮'] [@xxx=xxx] 标签属性的筛选


result = tree.xpath("/html/body/ol/li")

for li in result:
    # 从每个li中提取文字信息
    a_text = li.xpath('./a/text()')       # 在li中继续寻找，./表示相对查找，在li当前节点继续查找
    # 拿a标签里面href的值
    a_href = li.xpath('./a/@href')        # 拿到属性值，通过@
    print(a_href)

print(tree.xpath('/html/body/ul/li/a/@href'))     # 也可以拿到标签属性值

