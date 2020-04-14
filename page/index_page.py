"""
 # 1.根据文件名创建类名继承基类
 # 2.根据定位元素变量名和操作组成方法名
 # 3.调用基类方法完成元素定位及操作
"""

# 导包
import page
from base.base_page import BasePage


class IndexPage(BasePage):  # 1.根据文件名创建类名继承基类
    """首页封装"""

    def click_my(self):  # 2.根据定位元素变量名和操作组成方法名
        """点击我的方法"""
        # 3.调用基类方法完成元素定位及操作
        self.click_function(self.find_element_function(page.my))
