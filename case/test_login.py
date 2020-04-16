"""登录测试用例"""
import time

import allure
import pytest
from page.page_factory import PageFactory
from utils import get_driver


class TestLogin(object):
    """登录测试类"""
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
        # 登录成功用例
        # self.page_factory.index_page().click_my() # 点击我的跳转页面
        # self.page_factory.my_page().clik_login_link()# 点击登录连接跳转登录页面
        # self.page_factory.login_page().login_function("18739223899","123456") # 登录
        # self.page_factory.login_page().click_alert() # 点击确定弹框
        # # 断言昵称
        # element = self.page_factory.my_page().nickname_text()
        # assert "用户_4514" in element

        # 未注册
        self.page_factory.index_page().click_my()  # 点击我
        self.page_factory.my_page().clik_login_link()# 点击登录连接
        self.page_factory.login_page().login_function("13800000000","123456")# 登录

        # 捕捉异常
        try:
            # 断言
            toast_msg = self.page_factory.login_page().login_get_toast("账号还未注册")
            assert "账号还未注册" in toast_msg
        except AssertionError as e:
            # 获取时间戳
            new_time = time.strftime("%Y%m%d_%H%M%S")
            # 给allure报告添加截图断言失败时进行截图 的命令：allure serve report
            # f"./screenshot/info_{new_time}.png" 在Terminal里使用pytest执行，不然会报错
            # 如果在当前右键点击执行 路径要这样写f"../screenshot/info_{new_time}.png"
            self.driver.get_screenshot_as_file(f"./screenshot/info_{new_time}.png")  # 断言失败时进行截图
            # rb以二进制方式读取
            # allure.MASTER_HELPER.attach(文件名称, 读取文件内容,文件类型)
            with open(f"./screenshot/info_{new_time}.png", "rb")as f:
                allure.MASTER_HELPER.attach("my_info", f.read(), allure.MASTER_HELPER.attach_type.PNG)

            raise e # 当截图操作完成后，应该还远测试用例的真是结果，因此需要再主动抛出异常
