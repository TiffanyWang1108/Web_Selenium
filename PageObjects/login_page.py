"""
Name : login_page.py
Author  : Tiffany
Time : 2022/7/24 18:44
DESC: 
"""
from selenium.webdriver.common.by import By

from PageObjects.base_page import BasePage
from utils.log_utils import logger


class LoginPage(BasePage):
    """登录页面：用户登录"""
    _BASE_URL = "https://litemall.hogwarts.ceshiren.com/#/login"
    __INPUT__USERNAME = (By.NAME, 'username')
    __INPUT__PASSWORD = (By.NAME, 'password')
    __BTN__LOGIN = (By.XPATH, '//*[@id="app"]/div/form/button')

    def login(self):
        # 访问登录页
        logger.info("进入登录")

        # 输入“用户名”
        self.do_send_keys("manage", self.__INPUT__USERNAME)
        # 输入“密码”
        self.do_send_keys('manage123', self.__INPUT__PASSWORD)
        # 点击“登录”按钮
        self.do_find(self.__BTN__LOGIN).click()

        from PageObjects.home_page import HomePage
        return HomePage(self.driver)
