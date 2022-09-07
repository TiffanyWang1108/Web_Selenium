"""
Name : test_ActionChains.py
Author  : Tiffany
Time : 2022/7/13 16:02
DESC: 
"""
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from time import sleep


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        click_btn = self.driver.find_element(By.XPATH, '//input[@value="click me"]')
        dbl_click = self.driver.find_element(By.XPATH, '//input[@value="dbl click me"]')
        right_click = self.driver.find_element(By.XPATH, '//input[@value="right click me"]')
        # 链式写法
        # ActionChains(self.driver).move_to_element(click_btn).click(click_btn).perform()
        # ActionChains(self.driver).move_to_element(dbl_click).double_click(dbl_click).perform()
        # ActionChains(self.driver).move_to_element(right_click).context_click(right_click).perform()
        # 分布写法
        action = ActionChains(self.driver)
        # action.move_to_element(click_btn)
        action.click(click_btn)
        action.double_click(dbl_click)
        action.context_click(right_click)
        sleep(3)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_move_to(self):
        self.driver.get("https://cn.bing.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

        element = self.driver.find_element(By.CSS_SELECTOR, '#id_sc')
        action = ActionChains(self.driver)
        action.move_to_element(element)
        sleep(3)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        drag = self.driver.find_element(By.ID, "dragger")
        drop = self.driver.find_element(By.CLASS_NAME, 'item')

        # ActionChains(self.driver).drag_and_drop(drag, drop).perform()
        actions = ActionChains(self.driver)
        actions.click_and_hold(drag).release(drop)
        sleep(3)

    def test_input(self):
        self.driver.get("https://sahitest.com/demo/label.htm")
        e1 = self.driver.find_element(By.XPATH, '/html/body/label[1]/input')
        # e2 = self.driver.find_element(By.XPATH, '/html/body/label[2]/table/tbody/tr/td[2]/input')
        e1.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE)
        action.perform()
        sleep(3)
