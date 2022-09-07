"""
Name : web_interactions.py
Author  : Tiffany
Time : 2022/7/6 17:18
DESC: 
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# 元素操作
# def element_interactions():
#     """
#     元素的操作：点击、输入、清空
#     :return:
#     """
#     # 1.实例化driver对象
#     driver = webdriver.Chrome()
#     # 2.打开一个网页
#     driver.get("https://www.sogou.com/")
#     # 3.定位到输入框# 4.输入搜索值
#     driver.find_element(By.ID, "query").send_keys("霍格沃兹测试开发")
#     # 强制等待三秒
#     time.sleep(3)
#     # 5.清空输入框
#     driver.find_element(By.ID, "query").clear()
#     time.sleep(3)
#     # 6.再次输入
#     driver.find_element(By.ID, "query").send_keys("霍格沃兹测试开发")
#     # 点击搜索
#     driver.find_element(By.ID, "stb").click()


# 获取元素属性
def element_get_attr():
    # 1.实例化driver
    driver = webdriver.Chrome()
    # 2.打开网页
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # 3.定位一个元素
    web_element = driver.find_element(By.ID, "locate_id")
    # 4.打印这个元素对象
    # print(web_element)
    # 5.获取元素的文本信息
    # print(web_element.text)
    # 6.获取元素的属性
    res = web_element.get_attribute("name")
    print(res)


if __name__ == '__main__':
    element_get_attr()

