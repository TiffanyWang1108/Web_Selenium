"""
Name : test_baidu.py
Author  : Tiffany
Time : 2022/7/21 17:17
DESC: 
"""
import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


# 目标1：代码异常时， 打印截图、page_source
# 实现方法：try catch 配合截图/ page_source操作
# 问题：异常处理会影响用力本身的结果
# 解决方案：在exception之后抛除异常---raise Exception
# 问题：异常捕获处理方式代码和业务代码无关，无法耦合
# 解决方案：使用装饰器装饰用例或者相关方法，不体现在源码中

# 1.先把装饰器的架子打好
# 2.嵌套相关逻辑
# 问题：driver实例无法使用，装饰去需要先获取driver对象

def ui_exception_record(func):
    def inner(*args, **kwargs):
        # 获取被装饰方法的实例对象
        # 通过self就可以拿到声明的实例变量
        # 前提条件：被装饰方法是实例方法，实例需要有实例变量self.driver
        # driver = args[0].driver
        # 问题：TestBaidu has no attribute driver :被装饰函数还未执行，所以还没有self.driver
        # 解决方案一：获取driver 放在函数执行之后
        # 解决方案二：保证使用装饰器的时候，driver 已经声明
        # 将获取driver 放在setup_class中

        try:
            # 当被装饰方法/函数发生异常就捕获并做数据记录
            return func(*args, **kwargs)

        except Exception:
            # 出现异常的处理
            driver = args[0].driver
            print("出现异常")

            # # 截图操作
            timestamp = int(time.time())
            image_path = f"./images/image_{timestamp}.PNG"
            # # 截图
            driver.save_screenshot(image_path)
            # # # 将截图放到allure报告中
            allure.attach.file(image_path, name="picture",
                               attachment_type=allure.attachment_type.PNG)
            #
            # # 记录page_source
            page_source_path = f"./page_source/page_source_{timestamp}.html"
            with open(page_source_path, "w", encoding="u8") as f:
                f.write(driver.page_source)
            #
            # # 将page_source记录到allure报告中
            allure.attach.file(page_source_path, name="pagesource",
                               attachment_type=allure.attachment_type.TEXT)
            raise Exception

    return inner


class TestBaidu:
    def setup_class(self):
        self.driver = webdriver.Chrome()

    @ui_exception_record
    def find(self):
        return self.driver.find_element(By.ID, "su")

    # 当被测函数存在返回值时，返回值会丢失。
    # 解决方法：在try语句的被测函数中添加 return ,

    def test_baidu(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.find().click()
        self.driver.quit()
