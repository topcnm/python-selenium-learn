# coding:utf-8
from selenium.webdriver.common.keys import Keys
from TestLogin import LoginTest
from time import sleep
from random import randint
import unittest

'''
基于页面已经登录的场景
利用传入driver的方式，防止多个驱动
'''


class PurchaseTest(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver

    def test_save(self):
        print('Hi, now we start saving')

        # skip to 'Application Create' page
        self.driver.find_element_by_xpath("//a[@href='#/']").click()

        # skip to 'Purchase Create' page
        self.driver.find_element_by_xpath(
            "//a[@href='#/form/purchase/create']").click()

        # STEP 1 autoComplete 组件
        all_auto = self.driver.find_elements_by_class_name(
            "ant-select-search__field")
        self.test_auto_complete(all_auto[0])
        self.test_auto_complete(all_auto[2])

        # STEP 2 Select 组件
        all_select = self.driver.find_elements_by_class_name(
            "ant-select-selection__rendered")
        self.test_select(all_select[1])
        self.test_select(all_select[2])
        self.test_select(all_select[3])
        self.test_select(all_select[4])

        # STEP 3 DatePicker 组件
        fee_start_dp = self.driver.find_element_by_id("costDateFrom")
        fee_end_dp = self.driver.find_element_by_id("costDateTo")
        demand_dp = self.driver.find_element_by_id("demandDate")

        self.test_date_picker(fee_start_dp, 10)
        self.test_date_picker(fee_end_dp, 17)
        self.test_date_picker(demand_dp, 20)

        # STEP 4 INPUT textArea 组件

        self.driver.find_element_by_id('applyExplain').send_keys(
            'Auto Test Title-{}'.format(randint(1000, 9999)))
        self.driver.find_element_by_id("applyDescribe").send_keys(
            "If your see this content, means test run correctly")

        # STEP 5 Table information
        self.test_create_save_row()
        self.test_create_save_row()

        # STEP 6 保存表单
        save_btn = self.driver.find_element_by_id("purchaseSave")
        save_btn.click()

        sleep(10)

        # STEP 7 保存成功后跳转到myAppy
        my_apply_page_url = self.driver.current_url

        success_str = "backlog"
        self.assertIn(success_str, my_apply_page_url, msg="提交后未保存成功!!!")

        print("表单提交测试成功")

        self.driver.quit()

    def test_detail(self):
        pass

    def test_approve(self):
        pass

    def record_log(self):
        pass

    def test_select(self, element):
        sleep(2)
        element.click()
        self.driver.find_element_by_css_selector(
            ".ant-select-dropdown:not(.ant-select-dropdown-hidden) .ant-select-dropdown-menu-item").click()
        print("下拉框测试OK")

    def test_auto_complete(self, element):
        element.click()
        element.clear()
        element.send_keys('0')
        element.send_keys(Keys.BACK_SPACE)

        sleep(2)
        self.driver.find_element_by_css_selector(
            ".ant-select-dropdown:not(.ant-select-dropdown-hidden) .ant-select-dropdown-menu-item").click()
        print("智能匹配测试OK")

    def test_date_picker(self, element, index):
        element.click()
        sleep(3)
        self.driver.find_elements_by_class_name(
            "ant-calendar-date")[index].click()
        print("日期组件测试OK")

    def test_create_save_row(self):
        add_row_btn = self.driver.find_element_by_id("purchaseRowAdd")
        save_row_btn = self.driver.find_element_by_id("purchaseRowSave")

        add_row_btn.click()

        purchase_name_input = self.driver.find_elements_by_css_selector(
            ".ant-table .ant-input")[0]
        purchase_purpose_input = self.driver.find_elements_by_css_selector(
            ".ant-table .ant-input")[1]
        purchase_desc_input = self.driver.find_elements_by_css_selector(
            ".ant-table .ant-input")[2]

        purchase_count_input = self.driver.find_elements_by_css_selector(
            ".ant-table .ant-input-number-input")[0]
        purchase_price_input = self.driver.find_elements_by_css_selector(
            ".ant-table .ant-input-number-input")[1]

        purchase_name_input.send_keys("test content")
        purchase_purpose_input.send_keys("test purc")
        purchase_desc_input.send_keys("hahaha")
        purchase_count_input.clear()
        purchase_count_input.send_keys(1)
        purchase_price_input.clear()
        purchase_price_input.send_keys(2)

        save_row_btn.click()
        print("采购计划行数据创建OK")


if __name__ == '__main__':
    # public for test login
    login_page = LoginTest()
    login_page.test_login()

    purchase_case = PurchaseTest(login_page.driver)
    purchase_case.test_save()
