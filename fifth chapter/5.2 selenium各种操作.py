import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

broswer = webdriver.Chrome()

broswer.get('https://www.baidu.com/')

broswer.find_element(By.XPATH, '')

# 找到输入框，输入python  --> 输入回车/点击搜索按钮
# 找到输入框
# 找到输入框并输入python
time.sleep(2)   # 让浏览器缓一会，等所有东西都加载完在继续向下执行

broswer.find_element(By.XPATH, '').send_keys('python', Keys.ENTER)

# 思路： 查找存放数据的位置，进行数据提取
# 这里记录一下怎么查找多个元素

# 这个xpath的路径和用lxml方式一样
li_list = broswer.find_elements(By.XPATH, '')

for li in li_list:
    li.find_element()     # 元素还可以继续寻找
    # 元素的文本值怎么拿到
    # 教程中是这么获取的
    value = li.find_element(By.XPATH, '').text      # 看来能拿到

# 最终总结
# 这个东西挺好用的，但是也有局限，就是某些网站会针对selenium做检测，如果检测到是
# selenium，那么网站会不工作，这也算是局限性



