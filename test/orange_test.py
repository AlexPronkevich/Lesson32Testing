import unittest
from entity.orange import Orange


class OrangeTest(unittest.TestCase):
    def test_orange_default_constructor(self):
        orange = Orange()
        expected_diameter = 100
        expected_vitamin = 1000
        expected_cost = 0

        self.assertEqual(expected_diameter, orange.diameter)
        self.assertEqual(expected_vitamin, orange.vitamin)
        self.assertEqual(expected_cost, orange.price)

    def test_negative_orange_diameter(self):
        diameter = -200
        expected = 1000

        orange = Orange(vitamin=vitamin)

        self.assertEqual(expected, orange.vitamin)

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

