#!/usr/bin/python3

import unittest
from calc_mul import calc

class TestCalcAdditional(unittest.TestCase):

    # 正常系（同値分割）
    def test_valid(self):
        self.assertEqual(200, calc(20, 10))

    # 境界値（下限）
    def test_lower_boundary_ok(self):
        self.assertEqual(1, calc(1, 1))

    def test_lower_boundary_ng(self):
        self.assertEqual(-1, calc(0, 1))

    # 境界値（上限）
    def test_upper_boundary_ok(self):
        self.assertEqual(999*999, calc(999, 999))

    def test_upper_boundary_ng(self):
        self.assertEqual(-1, calc(1000, 1))

    # 型異常
    def test_string(self):
        self.assertEqual(-1, calc("10", 5))

    def test_float(self):
        self.assertEqual(-1, calc(1.5, 10))

    def test_none(self):
        self.assertEqual(-1, calc(None, 10))

    # A > B のケース（本来は正常だが現状はバグで -1）
    def test_a_greater_than_b(self):
        self.assertEqual(50, calc(10, 5))
