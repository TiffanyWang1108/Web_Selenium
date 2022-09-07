"""
Name : test_alert.py
Author  : Tiffany
Time : 2022/7/16 15:53
DESC: 
"""
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium_frame_window.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")

        drag = self.driver.find_element(By.ID, "draggable")
        drop = self.driver.find_element(By.ID, "droppable")

        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        sleep(2)
        print("点击alert确认")
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, "submitBTN").click()
        sleep(3)



