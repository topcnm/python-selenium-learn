# coding:utf-8
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep


class MeetingList(Page):
    """
    我的会议列表
    """

    url = "/honycloud/mrbs/manager/built/index.html#/meetingList"

    search_title_button_loc = (By.XPATH, "//span[@class='input-group-addon']")
    search_title_input_loc = (By.XPATH, "//span[@class='input-group']/form/input[@class='form-control']")

    def search_title(self, keyword):
        self.find_element(*self.search_title_input_loc).send_keys(keyword)

    def search_button(self):
        self.find_element(*self.search_title_button_loc).click()

    def search_something(self, keyword="bad_kw"):
        self.open()
        # pending the initial ajax
        sleep(2)
        self.search_title(keyword)
        self.search_button()
        sleep(2)

    def search_success(self):
        pass
