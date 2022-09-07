"""
Name : web_util.py
Author  : Tiffany
Time : 2022/7/25 0:06
DESC: 
"""


# 自定义显式等待条件
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utils.log_utils import logger


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


