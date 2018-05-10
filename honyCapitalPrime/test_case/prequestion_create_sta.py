# coding:utf-8
import unittest
import sys
from time import sleep
from models import myunit
from page_obj.loginPage import Login
from page_obj.prequestionPage import CreatePreQ


class CreatePreQuestionTest(myunit.MyUnitTest):
    u"""新建预提问页面"""
    create_success_url = '/preQuestionList'

    def pre_question_create_verify(self, topic="", remark=""):
        CreatePreQ(self.driver).test_create_pre_question(topic, remark)

    def test_create(self):
        u"""正常新建预提问测试"""
        self.pre_question_create_verify(
            topic="i am a test man",
            remark="this is robot action")
        sleep(3)
        page = CreatePreQ(self.driver)
        self.assertIn(
            self.create_success_url,
            page.on_url(),
            msg="creating pre question fail"
        )

    def test_create_no_topic_error(self):
        u"""异常新建预提问测试：未输入预提问主题"""
        self.pre_question_create_verify(
            topic="", remark="this is robot action")
        sleep(3)
        page = CreatePreQ(self.driver)
        self.assertNotIn(
            self.create_success_url,
            page.on_url(),
            msg="No topic, creating pre question fail"
        )

    def test_create_no_remark(self):
        u"""异常新建预提问测试：未输入预提问备注"""
        self.pre_question_create_verify(topic="Hi, honyCapital", remark="")
        sleep(3)
        page = CreatePreQ(self.driver)
        self.assertIn(
            self.create_success_url,
            page.on_url(),
            msg="No remark, creating pre question fail"
        )

    def setUp(self):
        super(CreatePreQuestionTest, self).setUp()
        Login(
            self.driver).user_login(
            username="otzhaomin",
            password="Password!")


if __name__ == '__main__':
    sys.path.append('..')
    from package import HTMLTestRunner

    suite = unittest.TestSuite()
    suite.addTest(CreatePreQuestionTest('test_create'))
    suite.addTest(CreatePreQuestionTest('test_create_no_topic_error'))
    suite.addTest(CreatePreQuestionTest('test_create_no_remark'))

    file_path = "../report/py_result.html"
    fp = open(file_path, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'新建预提问测试报告', description=u'这是报告说明')
    runner.run(suite)
    fp.close()
