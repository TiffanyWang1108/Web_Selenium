"""
Name : test_ceshiren.py
Author  : Tiffany
Time : 2022/7/11 9:28
DESC: 
"""


# 结合pytest测试框架
# 用例标题=文件名+类名+方法名
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCeshiren:
    # 前置处理
    def setup(self):
        """
        前提条件：进入测试人论坛的搜索页面
        测试步骤：1.输入搜索关键词
                2.点击搜索按钮
        """
        # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)  # 隐式等待
        self.driver.maximize_window()
        # 进入测试人论坛的搜索页面
        self.driver.get("https://ceshiren.com/search?expanded=true")

    # 后置处理
    def teardown(self):
        # 每次用例结束关闭chormedriver进程和浏览器
        self.driver.quit()

    def test_search(self):
        # 定位到搜索框输入搜索关键词
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="搜索"]').send_keys("Appium")
        # 定位到搜索按钮并点击
        self.driver.find_element(By.CLASS_NAME, "search-cta").click()
        # # 强制等待五秒
        # time.sleep(5
        # 获取文本类结果
        web_element = self.driver.find_element(By.CSS_SELECTOR, ".topic-title")
        # 断言appium是否在搜索结果中，，，.lower()--大写转小写
        assert 'Appium' in web_element.text

