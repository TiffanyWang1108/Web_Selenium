"""
Name : test_window.py
Author  : Tiffany
Time : 2022/7/13 20:53
DESC: 
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_frame_window.base import Base


class TestWindows(Base):

    def test_wondow(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.LINK_TEXT, "登录").click()
        print(self.driver.current_window_handle)
        self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)

        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])

        self.driver.find_element(By.CSS_SELECTOR, "#TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element(By.CSS_SELECTOR, "#TANGRAM__PSP_4__phone").send_keys("18884001218")

        sleep(2)
        self.driver.switch_to_window(windows[0])
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__changePwdCodeItem").click

        self.driver.find_element(By.ID, "TANGRAM__PSP_11__userName").send_keys("login_username")
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__password").send_keys("login_pwd")
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__submit").click

        sleep(3)
