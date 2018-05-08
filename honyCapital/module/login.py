# coding:utf-8
"""
    工具方法：用以登录登出
"""


class Login(object):
    def __init__(self):
        pass

    @staticmethod
    def user_login(driver, username, password):
        username_input = driver.find_element_by_id('idToken1')
        password_input = driver.find_element_by_id('idToken2')
        submit_button = driver.find_element_by_id('loginButton_0')

        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)

        submit_button.click()

    @staticmethod
    def user_logout(self):
        pass


if __name__ == '__main__':
    Login()
