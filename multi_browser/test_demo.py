"""
Name : test_demo.py
Author  : Tiffany
Time : 2022/7/29 11:08
DESC: 
"""
from selenium import webdriver

from multi_browser.conftest import web_env


class TestBroswer():
    def setup_class(self):
        self.broswer = web_env.get("broswer")

    def test_Ceshiren(self):
        print(f"获取到的浏览器信息为{self.broswer}")
        if self.broswer == "chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.firefox()

        self.driver.get("https://www.ceshiren.com")
        self.driver.quit()
