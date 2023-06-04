# Version 1.0
# Author: Pronkevich Alexandra
# Group: QA2022
# Date: 28.05.2023

import unittest
from entity.rose import Rose


class RoseTest(unittest.TestCase):
    def test_rose_default_constructor(self):
        rose = Rose()
        expected_color = "white"
        expected_weight = 1
        expected_price = 0

        self.assertEqual(expected_color, rose.color)
        self.assertEqual(expected_weight, rose.weight)
        self.assertEqual(expected_price, rose.price)

    def test_negative_rose_diameter(self):
        weight = -200
        eexpected = 1000

        rose = Rose(weight=weight)

        self.assertEqual(expected, rose.weight)

    # def test_negative_orange_cost(self):
    #     price = -200
    #     expected = 0
    #
    #     orange = Orange(cost=price)
    #
    #     self.assertEqual(expected, orange.price)

    def test_diameter_property_negative(self):
        orange = Orange()
        expected = orange.diameter
        orange.diameter = -200
        self.assertEqual(expected, orange.diameter)

    def test_diameter_property_positive(self):
        orange = Orange()
        expected = 200
        orange.diameter = 200
        self.assertEqual(expected, orange.diameter)

    def test_diameter_property_zero(self):
        orange = Orange()
        expected = orange.diameter
        orange.diameter = 0
        self.assertEqual(expected, orange.diameter)

    def test_vitamin_property_negative(self):
        orange = Orange()
        expected = orange.vitamin
        orange.vitamin = -200
        self.assertEqual(expected, orange.vitamin)

    def test_vitamin_property_positive(self):
        orange = Orange()
        expected = 200
        orange.vitamin = 200
        self.assertEqual(expected, orange.vitamin)

    def test_vitamin_property_zero(self):
        orange = Orange()
        expected = orange.vitamin
        orange.vitamin = 0
        self.assertEqual(expected, orange.vitamin)

