"""
Name : TestLitemall.py
Author  : Tiffany
Time : 2022/7/20 15:39
DESC: 
"""
import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

# 代码优化
# 1. 用例产生了脏数据需要清理----使用接口或ui方式进行清理
# 2. 代码出现了大量的强制等待----使用显式等待进行优化
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.log_utils import logger


class TestLitemall:
    def setup_class(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        # 添加隐式等待
        self.driver.implicitly_wait(3)
        # 窗口最大化
        self.driver.maximize_window()
        # 登录功能
        self.driver.get("https://litemall.hogwarts.ceshiren.com/#/login?redirect=%2Fdashboard")
        # 清空输入框，输入用户名
        self.driver.find_element(By.NAME, 'username').clear()
        self.driver.find_element(By.NAME, 'username').send_keys('manage')
        # 清空输入框，输入密码
        self.driver.find_element(By.NAME, 'password').clear()
        self.driver.find_element(By.NAME, 'password').send_keys('manage123')
        # 点击登录按钮
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/form/button').click()

    def teardown_class(self):
        # 关闭浏览器
        self.driver.quit()

    def get_screen(self):
        timestamp = int(time.time())
        image_path = f"./images/image_{timestamp}.PNG"
        # 截图
        self.driver.save_screenshot(image_path)
        # 将截图放进allure报告中
        allure.attach.file(image_path, name="picture", attachment_type=allure.attachment_type.PNG)

    def test_Add(self):
        # 点击商场管理/商品类目，进入商品类目页面
        # Xpath 文本定位
        self.driver.find_element(By.XPATH, '//*[text()="商场管理"]').click()
        self.driver.find_element(By.XPATH, '//*[text()="商品类目"]').click()
        self.driver.find_element(By.XPATH, '//*[text()="添加"]').click()
        # css表达式定位--classname一样的时候取定位的第一个
        self.driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys("新增商品")

        # 添加显式等待--
        # ele = WebDriverWait(self.driver, 10). \
        #     until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[text()="确定"]')))
        # ele.click()

        # 自定义显式等待条件
        def click_exception(by, element, max_Attempts=5):
            def _inner(driver):
                # 多次点击按钮
                actual_attempts = 0  # 实际点击次数起始0
                while actual_attempts < max_Attempts:  # 实际点击次数小于最大点击次数时，进行循环点击操作
                    actual_attempts += 1  # 实际点击次数每次加1
                    try:
                        # 执行点击操作
                        driver.find_element(by, element).click()
                        # 点击成功，直接return true 循环结束
                        logger.info(f"第{actual_attempts}次点击成功")
                        return True
                    # 点击失败，抛出异常
                    except Exception:
                        logger.debug(f"在第{actual_attempts}次点击时报错")
                # 实际点击次数超过最大点击次数，抛出异常
                raise Exception("超出最大点击次数")

            return _inner

        WebDriverWait(self.driver, 10).until(click_exception(By.XPATH, '//*[text()="确定"]'))

        # find_elements 如果没找到元素会返回空列表，find_element没找到元素报错
        res = self.driver.find_elements(By.XPATH, '//*[text()="新增商品"]')
        self.get_screen()
        # 添加断言 判断新增产品是否成功找到
        # 判断返回值是否为空列表
        assert res != []

    def test_delete(self):
        self.driver.find_element(By.XPATH, '//*[text()="商场管理"]').click()
        self.driver.find_element(By.XPATH, '//*[text()="商品类目"]').click()
        self.driver.find_element(By.XPATH, '//*[text()="添加"]').click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys("删除商品测试")
        ele = WebDriverWait(self.driver, 10). \
           until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[text()="确定"]')))
        ele.click()
        self.driver.find_element(By.XPATH, '//*[text()="删除商品测试"]/../..//*[text()="删除"]').click()
        # sleep(5)  # 添加强制等待，等待元素从页面消失再进行断言
        # 添加显式等待
        WebDriverWait(self.driver, 10).until_not(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                                    '//*[text('
                                                                                                    ')="删除商品测试"]')))
        # 若删除成功，find_elements 返回值应该为空列表
        res = self.driver.find_elements(By.XPATH, '//*[text()="删除商品测试"]')
        logger.info(f"获取到的结果为{res}")
        # 添加断言是否返回空列表
        assert res == []
