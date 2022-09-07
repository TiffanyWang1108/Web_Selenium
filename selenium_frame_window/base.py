"""
Name : base.py
Author  : Tiffany
Time : 2022/7/13 20:55
DESC: 
"""
import self as self
from selenium import webdriver


class Base:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
