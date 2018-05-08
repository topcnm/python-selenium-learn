# coding:utf-8
import unittest
from time import sleep
from models import myunit
from page_obj.loginPage import Login
from page_obj.prequestionPage import CreatePreQ


class CreatePreQuestionTest(myunit.MyUnitTest):
    """
    新建预提问
    """

    def pre_question_create_verify(self, topic="", remark=""):
        CreatePreQ(self.driver).test_create_pre_question(topic, remark)

    def test_create(self):
        self.pre_question_create_verify(topic="i am a test man", remark="this is robot action")
        sleep(3)
        page = CreatePreQ(self.driver)
        current_url = page.on_url()
        expected_url = '/preQuestionList'
        self.assertIn(expected_url, current_url, msg="creating pre question fail")

    def setUp(self):
        super(CreatePreQuestionTest, self).setUp()
        Login(self.driver).user_login(username="otzhaomin", password="Password!")


if __name__ == '__main__':
    unittest.main()
