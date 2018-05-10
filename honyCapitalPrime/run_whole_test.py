# coding:utf-8
from package import HTMLTestRunner
import unittest
import time


def send_email():
    pass


def new_report():
    pass


if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    file_name = './report/{} honyCapital_report_result.html'.format(now)
    fb = open(file_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title=u"弘毅云平台测试报告",
        description=u"环境：macOs, chrome"
    )

    discover = unittest.defaultTestLoader.discover(
        './test_case',
        pattern='*_sta.py'
    )

    runner.run(discover)
    fb.close()
