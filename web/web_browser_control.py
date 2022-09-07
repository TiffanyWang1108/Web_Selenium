"""
Name : web_browser_control.py
Author  : Tiffany
Time : 2022/7/5 17:07
DESC: 
"""
# 打开浏览器
import time

from selenium import webdriver


def open_browser():
    driver = webdriver.Chrome()
    # 调用get方法时需要传递url
    driver.get("https://www.ceshiren.com/")
    time.sleep(2)
    # 刷新浏览器
    # driver.refresh()
    # 退回操作
    # driver.get("https://www.baidu.com/")
    # driver.back()
    # 最大化
    driver.maximize_window()
    time.sleep(5)
    # 最小化
    driver.minimize_window()
    time.sleep(5)


if __name__ == '__main__':
    open_browser()
