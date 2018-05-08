# coding:utf-8
from selenium import webdriver


def browser():
    return webdriver.Chrome()


if __name__ == '__main__':
    tab = browser()
    tab.get("http://www.zhihu.com")
    tab.quit()
