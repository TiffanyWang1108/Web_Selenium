"""
Name : TestSearch.py
Author  : Tiffany
Time : 2022/7/23 14:04
DESC: 
"""
from PO_module.search_page import SearchPage


class TestSearch:
    def test_search(self):
        text = SearchPage().search_stock("阿里巴巴-sw")
        # 断言
        assert "阿里巴巴-sw" == text
