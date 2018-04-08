#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 14:01
# @Author  : Dirk Zhao
import yaml
import os
from utils.path_utils import CONFIG_PATH


def yaml_read():
    config_file = os.path.join(CONFIG_PATH, "config.yaml")
    with open(config_file) as f:
        d = yaml.load(f)
    return d
