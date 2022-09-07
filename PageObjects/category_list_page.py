"""
Name : category_list_page.py
Author  : Tiffany
Time : 2022/7/24 18:44
DESC: 
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.base_page import BasePage
from utils.log_utils import logger


class CategoryListPage(BasePage):
    """类目列表页面：点击添加"""
    __BTN_ADD = (By.XPATH, '//*[text()="添加"]')
    __MSG_ADD_OPERATE = (By.XPATH, "//p[contains(text(), '创建')]")
    __MSG_DELETE_OPERATE = (By.XPATH, "//p[contains(text(), '删除')]")

    def click_add(self):
        # 点击“添加”按钮
        logger.info("类目列表页面：点击添加")
        self.do_find(self.__BTN_ADD).click()

        # ==》创建类目页面
        from PageObjects.category_create_page import CategoryCreatePage
        return CategoryCreatePage(self.driver)

    """类目列表页面：获取操作结果"""

    def get_operate_result(self):
        logger.info("类目列表页面：获取操作结果")
        # 获取冒泡消息文本
        element = self.wait_element_until_visible(self.__MSG_ADD_OPERATE)
        # 获取消息文本
        msg = element.text
        logger.info(f"冒泡消息：{msg}")
        # ==》返回消息文本
        return msg

    def delete_category(self, category_name):
        logger.info("对指定类目进行删除")
        # 对指定类目进行删除
        self.do_find(By.XPATH, f"//*[text()='{category_name}']/../..//*[text()='删除']").click()
        # 跳转到当前页面
        return CategoryListPage(self.driver)

    def get_delete_result(self):
        # 获取冒泡消息文本
        element = self.wait_element_until_visible(self.__MSG_DELETE_OPERATE)
        # 获取消息文本
        msg = element.text
        logger.info(f"冒泡消息：{msg}")
        # ==》返回消息文本
        return msg

