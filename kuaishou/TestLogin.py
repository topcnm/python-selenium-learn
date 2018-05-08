# coding:utf-8
from selenium import webdriver
from module.login import Login
from time import sleep
import unittest


class LoginTest(unittest.TestCase):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://localhost:8083/#/login')

    def test_login(self):
        username = '00001'
        password = '1'

        login_page = Login()
        login_page.user_login(self.driver, username, password)

        # check login result
        return self.check_login()

    def check_login(self):
        login_name = self.driver.find_element_by_class_name(
            'nav-user-name').get_attribute('textContent')
        self.assertTrue(login_name.strip(), msg="Login fail")


if __name__ == '__main__':
    LoginTest().test_login()
