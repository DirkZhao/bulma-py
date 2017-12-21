#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 下午5:26
# @Author  : Dirk Zhao

from utils.config import Config

a = Config().get('server_url')
print(a)