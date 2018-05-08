# coding:utf-8
from selenium import webdriver
from module.login import Login
import unittest


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('https://uat.honycapital.com/honycloud/login.jsp')

    def test_login(self):
        username = 'otzhaomin'
        password = 'Password!'

        login_page = Login()
        login_page.user_login(self.driver, username, password)

        self.check_login()

    def check_login(self):
        current_url = self.driver.current_url
        expected_url = '/honycloud/main/index.do'
        self.assertIn(expected_url, current_url, msg="登录失败")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestLogin("test_login"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
