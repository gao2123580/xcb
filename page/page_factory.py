# 导包
from page.index_page import IndexPage
from page.login_page import LoginPage
from page.my_page import MyPage


class PageFactory(object):
    """统一入口类"""
    def __init__(self,driver):
        self.driver = driver

    def index_page(self):
        """首页"""
        return IndexPage(self.driver)

    def my_page(self):
        """我的页面"""
        return MyPage(self.driver)

    def login_page(self):
        """登录页面"""
        return LoginPage(self.driver)