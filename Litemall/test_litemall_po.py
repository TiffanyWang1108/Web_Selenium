"""
Name : TestLitemall.py
Author  : Tiffany
Time : 2022/7/20 15:39
DESC: 
"""
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.login_page import LoginPage
from utils.log_utils import logger


class TestLitemall:
    def setup_class(self):
        """登录页面：用户登录"""
        self.home = LoginPage().login()

    def teardown_class(self):
        self.home.do_quit()

    @pytest.mark.parametrize("category_name", ["新增商品测试1", "新增商品测试2"])
    def test_Add(self, category_name):
        # 测试用例
        # 添加商品类型:

        """系统首页：进入商品类目"""
        """类目列表页面：点击添加"""
        """创建类目页面：创建类目"""
        """类目列表页面：获取操作结果"""
        # 链式调用
        list_page = self.home \
            .go_to_category() \
            .click_add() \
            .create_category(category_name)
        # 将页面的操作结果用res存起来
        res = list_page.get_operate_result()
        assert "创建成功" == res
        # 执行数据清理
        list_page.delete_category(category_name)

    @pytest.mark.parametrize("category_name", ["delA", "delB", "c"])
    def test_delete(self, category_name):
        res = self.home \
            .go_to_category() \
            .click_add() \
            .create_category(category_name) \
            .delete_category(category_name) \
            .get_delete_result()
        print(res)
        assert res == "删除成功"
