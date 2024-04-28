# 有些平台有破解验证码的平台，教程中用的是超级鹰
# 用超级鹰干超级鹰
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from chaojiying import Chaojiying_Client

broswer = Chrome()

broswer.get('https://chaojiying.com/user/login')

# 先处理验证码
# 先找到验证码
# 截取屏幕, 就是选中的元素截成图片, 而且返回的就是字节流
img_content = broswer.find_element(By.XPATH, '').screenshot_as_png
chaojiying = Chaojiying_Client('', '', '')
img_res = chaojiying.PostPic(img_content, 1902)

pic_str = img_res['pic_str']

# 找到验证码的input框
broswer.find_element(By.XPATH, '').send_keys(pic_str)
time.sleep(5)
# 用户名
broswer.find_element(By.XPATH, '').send_keys()
time.sleep(5)
# 密码
broswer.find_element(By.XPATH, '').send_keys()
time.sleep(5)

# 找到登陆按钮，进行点击
broswer.find_element(By.XPATH, '').click()

