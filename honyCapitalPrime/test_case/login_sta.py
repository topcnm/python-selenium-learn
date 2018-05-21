# coding:utf-8
import unittest
from models import myunit
from page_obj.loginPage import Login


class LoginTest(myunit.MyUnitTest):
    u"""登录页面"""

    # test login
    def user_login_verify(self, username="", password=""):
        Login(self.driver).user_login(username, password)

    def test_login(self):
        u"""正常登录测试"""
        self.user_login_verify(username="xxxxx", password="xxxxx!")
        page = Login(self.driver)
        title = page.on_title()
        self.assertEqual(title, u'工作台')


if __name__ == '__main__':
    unittest.main()
