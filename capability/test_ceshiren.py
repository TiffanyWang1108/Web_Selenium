"""
Name : test_ceshiren.py
Author  : Tiffany
Time : 2022/7/25 18:21
DESC: 
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_ceshiren_grid():
    driver = webdriver.Chrome()
    driver.get("https://www.ceshiren.com")
    driver.implicitly_wait(3)
    login_text = driver.find_element(By.CSS_SELECTOR, ".login-button").text
    print(login_text)


def test_ceshiren():
    hogwarts_grid_url = "https://selenium-node.hogwarts.ceshiren.com/wd/hub"
    capabilities = {"browserName": "chrome", "browserVersion": "101.0"}
    # 配置信息
    # 实例化Remote，获取可以远程控制的driver实例对象
    # 通过 command_execute配置selenium hub 地址
    # 通过 desired_capabilities 添加配置信息
    driver = webdriver.Remote(
        command_executor=hogwarts_grid_url,
        desired_capabilities=capabilities
    )
    driver.implicitly_wait(5)
    driver.get("https://www.ceshiren.com/")
    # 输入框输入搜索内容{霍格沃兹测试学院}
    text = driver.find_element(By.CSS_SELECTOR, ".login-button").text
    # 点击搜索按钮
    print(text)
    time.sleep(3)
    driver.quit()
