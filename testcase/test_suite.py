#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午2:22
# @Author  : Dirk Zhao

import unittest
from testcase.test_mathfunc import TestMathFunc

if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_multi"), TestMathFunc("test_divide")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner
    runner.run(suite)