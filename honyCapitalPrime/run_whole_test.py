# coding:utf-8
from package import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import unittest
import time
import os


def send_email(filePath):
    f = open(filePath, 'rb')
    mail_body = f.read()
    f.close()

    msg_root = MIMEMultipart('related')
    msg_root['Subject'] = Header("AutoTest Report for HonyCapital EP {}".format(time.strftime("%Y-%m-%d")), 'utf-8')

    mail_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_root.attach(mail_html)

    mail_attach = MIMEText(mail_body, 'base64', 'utf-8')
    mail_attach["Content-Type"] = "application/octet-stream"
    mail_attach["content-Disposition"] = "attachment; filename=Attachment.html"
    msg_root.attach(mail_attach)

    smtp = smtplib.SMTP()
    smtp.connect("owa.corp.gome.com.cn")
    smtp.login("zhouwangsheng@gome.com.cn", "!abcd123")
    smtp.sendmail("zhouwangsheng@gome.com.cn", "zhouwangsheng@gome.com.cn", msg_root.as_string())
    smtp.quit()
    print('hahaha !!!')


def latest_report(absolutePath):
    """
    从一大堆文件里面找出最新修改的文件；即通过排序文件名
    """
    file_name_list = os.listdir(absolutePath)
    file_name_list.sort(key=lambda fn: os.path.getmtime(absolutePath + "/" + fn))
    return absolutePath + "/" + file_name_list[-1]


if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    absolute_path = "{}/report".format(os.getcwd())
    file_name = '{}/{} honyCapital_report.html'.format(absolute_path, now)
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

    latest_file = latest_report(absolute_path)
    send_email(latest_file)
