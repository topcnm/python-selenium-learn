# coding:utf-8
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep


class Login(Page):
    """
        用户登录
    """

    url = "/honycloud/login.jsp"

    login_username_loc = (By.ID, "idToken1")
    login_password_loc = (By.ID, "idToken2")
    login_button_loc = (By.ID, "loginButton_0")

    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    def user_login(self, username="bad_username", password="bad_password"):
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)

    login_success_user_loc = (By.ID, "currentUserId")

    def user_login_success(self):
        return self.find_element(*self.login_success_user_loc)
