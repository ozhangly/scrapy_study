# xpath 是xml文档中搜索内容的一门语言
# html是xml的一个子集
import requests
from lxml import etree

# xpath是神
xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周大强</nick>
        <nick class="joy">周大强</nick>
        <nick class="jolin">蔡依伦</nick>
        <div>
            <nick>惹了</nick>
        </div>
        <span>
            <nick>惹了1</nick>
            <div>
                <nick>惹了2</nick>
            </div>
        </span>
    </author>
    
    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
"""

tree = etree.XML(xml)
# book = tree.xpath('/book')                        # 拿到book节点
# book = tree.xpath('/book/name')                   # 拿到book下的name节点
# book = tree.xpath('/book/name/text()')            # text() 拿文本  野花遍地香
# book = tree.xpath('/book/author/nick/text()')     # 输出的是['周大强', '周大强', '周大强', '蔡依伦']，但是如果也想要输出“惹了”，应该怎么办呢？
# 也就是多级孩子节点，这个多级是递归进行的，也就是能够拿到不管几代的后代都可以
# book = tree.xpath('/book/author//nick/text()')      # ['周大强', '周大强', '周大强', '蔡依伦', '惹了']
# book = tree.xpath('/book/author/*/nick/text()')     # * 任意的节点： 通配符     ['惹了', '惹了1']
book = tree.xpath('/book//nick/text()')

print(book)


