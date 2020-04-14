"""元素统一文件"""
from selenium.webdriver.common.by import By

# 首页页面定位元素
my = (By.XPATH,'//*[contains(@text,"我的")]') # 我的

# 我的页面定位元素
login_link = (By.XPATH,'//*[contains(@text,"登录/注册")]') # 登录祖册

nickname = (By.XPATH,"//*[contains(@text,'用户_4514')]")# 用户昵称

# 登录页面定位元素
user = (By.ID,"com.bjcsxq.chat.carfriend:id/login_phone_et")# 用户
pwd = (By.ID,"com.bjcsxq.chat.carfriend:id/login_pwd_et")# 密码
login_btn = (By.ID,"com.bjcsxq.chat.carfriend:id/login_btn") # 登录按钮
alert = (By.XPATH,"//*[@text='确定']")# 弹窗

