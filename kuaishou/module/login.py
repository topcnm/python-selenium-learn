# coding:utf-8


class Login(object):
    def __init__(self):
        pass

    @staticmethod
    def user_login(driver, username, password):
        driver.find_element_by_id('username').clear()
        driver.find_element_by_id('username').send_keys(username)
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys(password)

        driver.find_element_by_class_name("login-form-button").click()
        print('*' * 50)

    @staticmethod
    def user_logout(driver):
        driver.find_element_by_class_name("nav-user-name").hover()
        print('*' * 50)
        driver.quit()


if __name__ == '__main__':
    Login()
