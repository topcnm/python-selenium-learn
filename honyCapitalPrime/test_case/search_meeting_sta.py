# coding:utf-8
import unittest
from time import sleep
from models import myunit
from page_obj.loginPage import Login
from page_obj.meetingListPage import MeetingList


class SearchMeetingTest(myunit.MyUnitTest):
    u"""会议列表页面"""

    def keyword_search_verify(self, keyword=""):
        MeetingList(self.driver).search_something(keyword)

    def test_search(self):
        u"""正常会议列表搜索测试"""
        self.keyword_search_verify(keyword=u'汗毛竖起')

    def setUp(self):
        super(SearchMeetingTest, self).setUp()
        Login(self.driver).user_login(username="otzhaomin", password="Password!")


if __name__ == '__main__':
    unittest.main()
