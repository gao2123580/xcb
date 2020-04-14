import time
import pytest

from page.page_factory import PageFactory
from utils import get_driver


class TestLogin(object):
    """测试类"""
    @pytest.fixture(autouse=True)
    def before_function(self):
        # 获取驱动对象
        self.driver = get_driver()
        self.page_factory = PageFactory(self.driver)# 实例化统一入口类
        yield  # 结束
        # time.sleep(3)
        self.driver.quit() # 关闭驱动对象

    def test_login(self):
        """登录测试方法"""
        # 点击我的跳转页面
        self.page_factory.index_page().click_my()
        # 点击登录连接跳转登录页面
        self.page_factory.my_page().clik_login_link()
        # 输入账号密码
        self.page_factory.login_page().login_function("18739223899","123456")
        # 断言昵称
        element = self.page_factory.login_page().nickname_text()
        assert "用户_4514" in element

