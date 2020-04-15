"""PO文件基类"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self,driver):
        #  封装代码过程中，如果需要驱动对象，直接编写此方法
        self.driver = driver
    def find_element_function(self,location,timeout=5,poll=.05): # location 为元组类型数据
        """
        元素定位方法
        :param location: 元素定位信息
        :param timeout: 超长时间
        :param poll: 定位元素执行间隔时间
        :return:元素对象
        """
        # 添加显示等待
        element = WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll)\
            .until(lambda x: x.find_element(location[0],location[1]))
        return element

    def input_function(self,element,text):
        """
        元素输入方法
        :param element:元素对象
        :return:无
        """
        element.clear()# 先清空
        element.send_keys(text)# 输入

    def click_function(self,element):
        """
        点击方法
        :param element: 传元素对象
        :return:无
        """
        element.click() # 点击

    def get_toast_function(self,text):
        """获取toast信息方法"""
        # 处理传进来的定位信息
        # xpath ="//*[contains(@text,'再次点击')]"
        xpath = By.XPATH,"//*[contains(@text,{})]".format(text) # 这里不能写死
        # 调用当前类中定位方法
        element = self.find_element_function(xpath)
        # 返回目标元素的text属性值
        return element.text

        # 显示等待
        # element = WebDriverWait(driver, 3, .5) \
        #     .until(lambda x: x.find_element_by_xpath("//*[contains(@text,'再次点击')]"))
        # print(element.text)


