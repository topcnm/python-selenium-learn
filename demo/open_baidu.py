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


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

web_title = driver.title

# 模拟断言
if web_title == u'百度一下，你就知道':
    print('就这样判断啊，已经打开了')

