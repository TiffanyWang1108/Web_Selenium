"""
Name : web_locate.py
Author  : Tiffany
Time : 2022/7/6 14:47
DESC: 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


def web_locate():
    # 实例化driver对象
    driver = webdriver.Chrome()
    # 打开一个网页
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # 1.ID定位--第一个参数：定位方式；第二个参数：定位元素,返回值为webelement
    # Web_Element = driver.find_element(By.ID, "locate_id")
    # 2.Name定位
    # Web_Element = driver.find_element(By.NAME, "locate")
    # 3. css选择器定位：
    # Web_Element = driver.find_element(By.CSS_SELECTOR, "#locate_id > a > span")
    # 4. xpath定位
    # Web_Element = driver.find_element(By.XPATH,  '//*[@id="locate_id"]/a/span')
    # 5. 通过链接文本，a标签的span
    Web_Element = driver.find_element(By.LINK_TEXT, "元素定位")
    print(Web_Element)


if __name__ == '__main__':
    web_locate()
