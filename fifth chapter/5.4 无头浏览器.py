import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

broswer = Chrome()

broswer.get('某个网站')

# 定位到下拉列表
# 这个获取到的是HTML节点
sel = broswer.find_element(By.XPATH, '')

# 通过引入Select模块, 对元素进行包装成下拉菜单
sel = Select(sel)

# 让浏览器进行调整选项
# 这个sel指的是下拉框，options指的就是sel中的option
for i in range(len(sel.options)):       # i就是每个下拉框选项的索引位置
    sel.select_by_index(i)              # 根据索引进行选择
    # sel.select_by_value()             # 按照option中的value进行选择
    # sel.select_by_visible_text()      # 按照看到的字进行切换
    # 每次选择完select都会发送请求，所以切换完就睡一会
    time.sleep(3)
    # 然后就可以进行数据提取了
    table = broswer.find_element(By.XPATH, '')
    print(table.text)       # 打印所有文本信息

# <select>
#     <option value="1">哈哈</option>     看到的字是哈哈
#     <option value="xxx">2</option>
#     <option value="xxx">2</option>
#     <option value="xxx">2</option>
#     <option value="xxx">2</option>
# </select>
# 这个是select的基本构成

# 如果不想看到界面了，该怎么做?
# 准备好参数配置
opt = Options()
opt.add_argument('--headless')
# 禁用gpu
opt.add_argument('--disable-gpu')

broswer = Chrome(options=opt)


# 如果想拿到页面代码怎么做？(这个代码是经过数据加载以及js执行之后的结果的html代码)
page_code = broswer.page_source     # 这个就是页面的代码

