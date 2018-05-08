# coding:utf-8
from TestLogin import TestLogin
import unittest


class TestLogout(unittest.TestCase):
    # 往往登录后case依赖于登录case
    def setUp(self):
        pass

    def test_logout(self):
        logout_button = self.driver.find_element_by_xpath("//a[@onclick='exitLogin();']")
        logout_button.click()

        logout_confirm = self.driver.find_element_by_css_selector(".exitLogin .btn-primary")
        logout_confirm.click()

        self.check_logout()

    def check_logout(self):
        current_url = self.driver.current_url
        expected_url = 'honycloud/login.jsp'
        self.assertIn(expected_url, current_url, msg="登出失败")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    # precondition 'login'
    suite = unittest.TestSuite()
    # suite.addTest(TestLogin("test_login"))
    suite.addTest(TestLogout("test_logout"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
