"""
Name : wait_demo.py
Author  : Tiffany
Time : 2022/7/11 19:46
DESC: 
"""
import time

from selenium.webdriver.support.wait import WebDriverWait

if __name__ == '__main__':
    driver = 'driver111'


    def fake_condition(driver):
        print('当前的时间为，', time.time())
        # until传入的是函数对象不是函数调用
    WebDriverWait(driver, 10, 2).until(fake_condition, "霍格沃兹测试开发")
