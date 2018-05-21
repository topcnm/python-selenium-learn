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
from selenium.webdriver.common.by import By
import unittest
import time


class OpenBaidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")

    def tearDown(self):
        self.driver.quit()

    search_input_loc = (By.ID, 'kw')
    search_button_loc = (By.ID, 'su')

    def test_open_baidu(self):
        self.assertEqual(self.driver.title, u'百度一下，你就知道', msg='打不开啊！！')

    def test_search_baidu(self, keywords='selenium'):
        self.driver.find_element(*self.search_input_loc).send_keys(keywords)
        self.driver.find_element(*self.search_button_loc).click()
        time.sleep(2)
        self.assertEqual(
            self.driver.title,
            u"{}_百度搜索".format(keywords),
            msg=u'搜索失败')


if __name__ == '__main__':
    unittest.main()
