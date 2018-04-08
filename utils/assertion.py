#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/17 09:34
# @Author  : Dirk Zhao


def assertHttpCode(reponse, code_list=None):
    res_code = reponse.status_code
    if not code_list:
        code_list = [200]
    if res_code not in code_list:
        raise AssertionError('响应code不在列表中！')