"""
Name : chrome_remote.py
Author  : Tiffany
Time : 2022/7/21 13:02
DESC: 
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 定义配置的实例对象option
option = Options()
# 修改实例属性为 使用debug模式启动的 ip+端口号
option.debugger_address = "localhost:9222"
# 实例化driver的时候添加option配置参数，
driver = webdriver.Chrome(options=option)
driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
