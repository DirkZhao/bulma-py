#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 下午1:47
# @Author  : Dirk Zhao

from utils.config import Config, DRIVER_PATH

host = Config().get('TEST_HOST')
URL = 'http://oc.'+host
print(URL)