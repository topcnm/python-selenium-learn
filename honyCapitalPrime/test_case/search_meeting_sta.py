# coding:utf-8
import unittest
from time import sleep
from models import myunit
from page_obj.loginPage import Login
from page_obj.meetingListPage import MeetingList


class SearchMeetingTest(myunit.MyUnitTest):
    """
    搜索测试
    """

    def keyword_search_verify(self, keyword=""):
        MeetingList(self.driver).search_something(keyword)

    def test_search(self):
        self.keyword_search_verify(keyword=u'汗毛竖起')

        sleep(10)

    def setUp(self):
        super(SearchMeetingTest, self).setUp()
        Login(self.driver).user_login(username="otzhaomin", password="Password!")


if __name__ == '__main__':
    unittest.main()
