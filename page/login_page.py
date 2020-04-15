# 导包
import page
from base.base_page import BasePage

class LoginPage(BasePage):

    def input_user(self,username):
        """输入用户名方法"""
        self.input_function(self.find_element_function(page.user),username)

    def input_pwd(self,password):
        """输入密码方法"""
        self.input_function(self.find_element_function(page.pwd),password)

    def click_login_btn(self):
        """点击登录按钮方法"""
        self.click_function(self.find_element_function(page.login_btn))

    def click_alert(self):
        """点击确定弹框方法"""
        self.click_function(self.find_element_function(page.alert))

    def login_function(self,username,password):
            """登录定位统一方法"""
            self.input_user(username) # 用户
            self.input_pwd(password) # 密码
            self.click_login_btn() # 登录按钮
            self.click_alert()# 确定弹框