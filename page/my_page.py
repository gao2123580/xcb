# 导包
import page
from base.base_page import BasePage


class MyPage(BasePage):
    """我的页面封装类"""

    def clik_login_link(self):
        """点击登录/注册链接方法"""
        self.click_function(self.find_element_function(page.login_link))
