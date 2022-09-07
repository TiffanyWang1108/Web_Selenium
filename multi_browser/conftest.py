"""
Name : conftest.py
Author  : Tiffany
Time : 2022/7/29 11:10
DESC: 
"""
from _pytest.config import Config
from _pytest.config.argparsing import Parser

web_env = {}


def pytest_addoption(parser: Parser):
    # 注册一个命令组
    hogwarts = parser.getgroup("hogwarts")
    # 第一个参数为指定的命令行的参数的形式
    # 注册一个命令行参数
    hogwarts.addoption("--broswer", default="Chrome", dest="browser", help="指定执行的浏览器")


def pytest_configure(config: Config):
    broswer = config.getoption("browser")
    print(f"通过命令行获取到的浏览器为{broswer}")
    web_env["broswer"] = broswer
