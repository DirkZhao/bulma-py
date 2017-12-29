#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 下午3:30
# @Author  : Dirk Zhao
import unittest
from macaca import WebDriver
from utils.config import Config, DRIVER_PATH, DATA_PATH
from utils.log import logger
from utils.file_reader import ExcelReader


desired_caps = Config().get('desired_caps')
server_url = Config().get('server_url')


class LoginTest(unittest.TestCase):
    excel = '/Users/dirkzhao/macaca/bulma-py/data/username.xls'
    url = 'http://manager-center.imcoming.com/passport/login'

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver(desired_caps, server_url)
        cls.driver.init()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    def test_get_url(self):
        self.driver.get(self.url)

    def test_login(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                # 点击下拉框
                self.driver.element_('Xpath', "/html/body/div[1]/div/form/div[1]/div/div/div[1]/i").click()
                self.driver.wait_for(1000)
                # 选择手机验证码登录
                self.driver.wait_for_element('Xpath', "/html/body/div[2]/div/div[1]/ul/li[2]").click()
                self.driver.wait_for(1000)
                # 获取验证码
                self.driver.wait_for_element('Xpath', "/html/body/div[1]/div/form/div[2]/div[1]/div/div[1]/input").sendKeys(d['user'])
                self.driver.wait_for_element('Xpath', "/html/body/div[1]/div/form/div[2]/div[2]/div/div/div/button").click()


if __name__ == '__main__':
    unittest.main()