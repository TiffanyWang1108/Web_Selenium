"""
Name : category_create_page.py
Author  : Tiffany
Time : 2022/7/24 18:45
DESC: 
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.base_page import BasePage
from utils.log_utils import logger
from utils.web_util import click_exception


class CategoryCreatePage(BasePage):
    """创建类目页面：创建类目"""
    __INPUT_CATEGORY_NAME = (By.CSS_SELECTOR, ".el-input__inner")
    __BTN_CONFIFRM = (By.XPATH, '//*[text()="确定"]')

    def create_category(self, category_name):
        logger.info("创建类目页面：创建类目")
        # 输入类目名称
        self.do_send_keys(category_name, self.__INPUT_CATEGORY_NAME)
        # 点击确定按钮
        WebDriverWait(self.driver, 10).until(click_exception(*self.__BTN_CONFIFRM))
        print("点击确定")

        # ==》类目列表页面
        from PageObjects.category_list_page import CategoryListPage
        return CategoryListPage(self.driver)
