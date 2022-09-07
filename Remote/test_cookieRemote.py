"""
Name : test_cookieRemote.py
Author  : Tiffany
Time : 2022/7/21 16:12
DESC: 
"""
import time

import yaml
from selenium import webdriver


class TestCookieLogin:
    def setup_class(self):
        self.driver = webdriver.Chrome()

    def test_get_cookies(self):
        # 访问企业微信登陆页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        # 等待三十秒。人工扫码
        time.sleep(30)
        # 成功登录后，获取cookie信息
        cookie = self.driver.get_cookies()
        print(cookie)
        # 将cookie存入一个可持久存储的地方，
        # 新建的文件注意添加write权限
        with open("cookie.yaml", "w") as f:
            # 第一个参数就是要写入的数据
            yaml.safe_dump(cookie, f)

    # 植入cookie
    def test_add_cookie(self):
        # 1.访问登陆页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        # 2.定义cookie，cookie信息从文件中获取
        cookie = yaml.safe_load(open("cookie.yaml"))
        # 3.植入cookie
        for c in cookie:
            self.driver.add_cookie(c)
        time.sleep(3)
        # 4.再次访问，无需扫码登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
