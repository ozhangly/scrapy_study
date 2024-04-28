import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


broswer = Chrome()

broswer.get('www.lagou.com')

broswer.find_element('xpath', '').click()

# 等等一系列操作后.....

# 当点击了一个元素，如果产生了一个新窗口，那么该如何处理

# 如何进到新窗口中进行提取
# 在selenium的眼中，新窗口默认是不切换过来的。

# 这个window_handles 对应的是浏览器上的选项卡
broswer.switch_to.window(broswer.window_handles[-1])

# 在新窗口中提取内容
content = broswer.find_element(By.XPATH, '').text

# 那么如何再回去呢

# 这里需要注意的是，就算关了这个标签页，视角还是在那个新开的标签页，还需要再
# 切换回去
broswer.close()
# 变更selenium 视角回开始的标签页
broswer.switch_to.window(broswer.window_handles[0])

# selenium除了标签页的切换，其中还有一种切换
broswer.get('xxx.xxxx.com/xxxx.html')

# 如果页面中遇到了iframe，如何进行处理
# 如果想拿到iframe中的内容，需要先把视角定位到iframe中，才能提取其中的内容
# 处理iframe的话，必须先拿到iframe，然后切换视角到iframe，再然后才能拿数据

# 找到iframe
iframe = broswer.find_element(By.XPATH, '')
# 进到iframe
broswer.switch_to.frame(iframe)
# 在进行find操作，就是在iframe中找东西了
tx = broswer.find_element(By.XPATH, '').text  # 在iframe中找东西
print(tx)

# 切到iframe里了，那如何再切出来
# 这个是切换到默认的内容，默认的内容就是开始的页面
broswer.switch_to.default_content()
# 以上iframe切换内容用到的不多
