# coding:utf-8
"""
    编程语言 python --------------------------
            |         |
            |    测试工具selenium
            |         |
            |    web驱动webdriver        +        浏览器驱动Chrome
            |         |
            |    测试案例 本例
            |
    断言 unittest
"""
from selenium import webdriver
import unittest


class OpenBaidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_open_baidu(self):
        self.driver.get("http://www.baidu.com")
        self.assertEqual(self.driver.title, u'百度一下，你就知道', msg='打不开啊！！')


if __name__ == '__main__':
    unittest.main()
