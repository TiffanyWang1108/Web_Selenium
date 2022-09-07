"""
Name : web_by_conditions.py
Author  : Tiffany
Time : 2022/7/12 19:46
DESC: 
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# 输入一：需要点击的目标按钮
# 输入二：下一个页面的某个元素

def multi_click(target_element, next_element):
    def _inner(driver):
        driver.find_element(*target_element).click()
        # 找到：return 的对象为webelement对象
        # 未找到：driver.find_element(*next_element)代码报错
        # 被until 循环中的异常捕获逻辑捕获异常，继续循环
        return driver.find_element(*next_element)

    return _inner


def wait_until():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # 使用官方提供的expected condition 语法满足需求
    # 需要自己封装期望条件：按钮需要点击多次才会出现弹框
    # 设计：多次点击按钮直到满足条件
    WebDriverWait(driver, 10).until(
        multi_click(
            (By.ID, 'primary_btn'),
            (By.XPATH, "//*[text()='该弹窗点击两次后才会弹出']")
        ))
    time.sleep(10)


if __name__ == '__main__':
    wait_until()
