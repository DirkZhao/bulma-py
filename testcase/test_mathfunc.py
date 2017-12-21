#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午2:23
# @Author  : Dirk Zhao

import unittest
from testcase.mathfunc import *


class TestMathFunc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(1, 2))

    def test_minus(self):
        self.assertEqual(1, minus(9, 8))

    def test_multi(self):
        self.assertEqual(10, multi(2, 5))

    def test_divide(self):
        self.assertEqual(2, divide(8, 4))
        self.assertEqual(2.5, divide(5, 2))


if __name__ == '__main__':
    unittest.main()
