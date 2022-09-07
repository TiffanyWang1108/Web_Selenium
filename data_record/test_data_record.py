"""
Name : test_data_record.py
Author  : Tiffany
Time : 2022/7/19 15:38
DESC: 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from data_record.log_utils import logger


class TestDataRecord:
    def setup(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_log_data_record(self):
        search_content = "霍格沃兹测试开发"
        self.driver.get("https://www.sogou.com/")
        self.driver.find_element(By.ID, 'query').send_keys(search_content)
        logger.debug(f"搜索的信息为{search_content}")
        self.driver.find_element(By.ID, 'stb').click()
        # 取第一条搜索结果进行断言
        search_result = self.driver.find_element(By.CSS_SELECTOR, 'em')
        logger.info(f"实际结果为{search_result.text}, 预期结果为{search_content}")
        assert search_result.text == search_content


