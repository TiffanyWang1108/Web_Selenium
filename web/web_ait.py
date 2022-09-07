"""
Name : web_ait.py
Author  : Tiffany
Time : 2022/7/6 15:36
DESC: 
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_show():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # 显式等待：解决元素交互问题
    # 参数：driver, 最长等待时间.until(结束条件)
    # expected_conditions的参数传入的都是一个元组
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "success_btn")))
    driver.find_element(By.ID, "success_btn").click()
    time.sleep(5)


if __name__ == '__main__':
    wait_show()
