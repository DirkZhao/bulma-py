#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 10:08
# @Author  : Dirk Zhao
import unittest
import time
from macaca import WebDriver,WebElement


desired_caps = {
    'platformName': 'Android',
    'deviceName': '',
    'app': '',
    'udid': '',
    'reuse': 3
}

server_url = {
    'hostname': 'localhost',
    'port': 3456
}

class Login(unittest.TestCase):
    def __init__(self):
