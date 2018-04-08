#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 14:07
# @Author  : Dirk Zhao
import os


def base_path(base_name):
    curdir = os.path.abspath(os.path.curdir)
    dirlist = curdir.split(os.path.sep)
    path = ''
    for dir in dirlist[1:]:
        path = path + os.path.sep + dir
        if dir == base_name:
            return path


BASE_PATH = base_path('bulma_py')
CONFIG_PATH = os.path.join(BASE_PATH, 'config')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')