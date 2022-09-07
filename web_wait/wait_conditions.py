"""
Name : wait_conditions.py
Author  : Tiffany
Time : 2022/7/12 18:28
DESC: 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_until():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # 确定返回值是否为webelement对象要进入condition中的源码进行查看
    # 不是所有的expected_conditions的返回值都是webelement
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, '#success_btn')))
    driver.find_element(By.CSS_SELECTOR, "#success_btn").click()


if __name__ == '__main__':
    wait_until()


# visible of elements locate any elements can be located
