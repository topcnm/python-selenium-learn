# coding:utf-8
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep


class CreatePreQ(Page):
    """
    创建预提问，用webdriver 描述页面元素的交互行为，以及用户可能存在的业务行为；
    页面变更时，只需要修改这一层即可
    loc: locator 定位器
    """

    url = "/honycloud/mrbs/manager/built/index.html#/addNewPreQ"

    preQ_topic_input_loc = (By.XPATH, "//input[@maxlength='50']")

    preQ_expire_button_loc = (By.CLASS_NAME, "input-group-addon")
    preQ_expire_date40_loc = (By.XPATH, "//table[@class='table-condensed']/tbody/tr[5]/td[5]")

    preQ_remark_input_loc = (By.XPATH, "//textarea[@maxlength='3000']")
    preQ_project_button_loc = (By.CLASS_NAME, "add_preQuesStyle")
    preQ_project_modal_first_radio_loc = (By.XPATH, "//input[@name='projectOne']")
    preQ_project_modal_confirm_button_loc = (By.CSS_SELECTOR, ".modal-footer .btn-primary")
    preQ_confirm_button_loc = (By.CSS_SELECTOR, ".btn-toolbar .btn-primary")

    def pre_question_topic(self, topic):
        self.find_element(*self.preQ_topic_input_loc).send_keys(topic)

    def pre_question_date_trigger(self):
        self.find_element(*self.preQ_expire_button_loc).click()

    def pre_question_date_day(self):
        self.find_element(*self.preQ_expire_date40_loc).click()

    def pre_question_remark(self, remark):
        self.find_element(*self.preQ_remark_input_loc).send_keys(remark)

    def pre_question_project_button(self):
        self.find_element(*self.preQ_project_button_loc).click()

    def pre_question_project_modal_radio(self):
        self.find_element(*self.preQ_project_modal_first_radio_loc).click()

    def pre_question_project_modal_confirm(self):
        self.find_element(*self.preQ_project_modal_confirm_button_loc).click()

    def pre_question_confirm(self):
        self.find_element(*self.preQ_confirm_button_loc).click()

    def test_create_pre_question(self, topic="bad_topic", remark="bad_remark"):
        self.open()
        self.pre_question_topic(topic)

        self.pre_question_date_trigger()
        sleep(1)
        self.pre_question_date_day()

        self.pre_question_remark(remark)
        self.pre_question_project_button()

        sleep(2)
        self.pre_question_project_modal_radio()
        self.pre_question_project_modal_confirm()

        sleep(1)
        self.pre_question_confirm()
        sleep(1)

    def test_create_success(self):
        return self.on_title()
