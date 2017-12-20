#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午2:23
# @Author  : Dirk Zhao

import unittest
from testcase.mathfunc import *

class TestMathFunc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(3,add(1,2))
        self.assertNotEqual(3,add(1,2))

