import time

from selenium.webdriver import Chrome
# 事件链
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from chaojiying import Chaojiying_Client


# 如果程序被识别到了，该怎么办？
# 第一种：chrome的版本号如果小于88      在程序启动浏览器时，此时没有加载任何网页内容的时候, 向页面嵌入js代码，去掉webdriver

# 第二种： chrome的版本号如果大于88
# 引入Option
option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')

# 一般是通过判断window.navigator.webdriver进行判断的
broswer = Chrome(option)

broswer.get('12306的网址')

time.sleep(10)

# 切换到账密登陆
broswer.find_element(By.XPATH, '').click()
# 再等一会
time.sleep(13)

# 先处理验证码
# 找到验证码的图片
verify_img = broswer.find_element(By.XPATH, '')
chaojiying = Chaojiying_Client('', '', '')

# 用超级鹰识别验证码
verify_res = chaojiying.PostPic(verify_img.screenshot_as_png, 9004)
axis = verify_res['pic_str']   # x1, y1 | x2, y2 | x3, y3
axis = axis.split('|')
for rs in axis:
    print(rs)           # x1,y1
    # 再对逗号切
    temp = rs.split(',')
    x = int(temp[0])
    y = int(temp[1])
    # 怎么打点?
    # 需要移动鼠标到某个位置，然后进行点击
    # 移动到一个节点并且带相对元素偏移量的位置
    # 这些都是定义好一些事件，具体的动作还没开始执行
    # 如果要开始执行动作，就perform()执行动作
    ActionChains(broswer).move_to_element_with_offset(to_element=verify_img, xoffset=x, yoffset=y).click().perform()

time.sleep(3)

# 输入用户名和密码
broswer.find_element(By.XPATH, '').send_keys('')
time.sleep(5)
broswer.find_element(By.XPATH, '').send_keys('')

time.sleep(3)
# 点击登陆
broswer.find_element(By.XPATH, '').click()

# 滑动验证怎么实现?
btn = broswer.find_element(By.XPATH, '')
# 抓起来，移动相对偏移量然后放下
# 纵向移动为0
ActionChains(broswer).drag_and_drop_by_offset(btn, 300, 0).perform()

