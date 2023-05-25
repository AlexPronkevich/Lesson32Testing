import unittest

from container.basket import Basket
from entity.product import Product
from logic.shop_assistance import ShopAssistance


class ShopAssistanceTest(unittest.TestCase):
    def test_different_type(self):
        basket = "string"
        expected = 0

        actual = ShopAssistance.calculate_total_price(basket)

        self.assertEqual(expected, actual)

    def test_empty_type(self):
        basket = Basket()
        expected = 0

        actual = ShopAssistance.calculate_total_price(basket)

        self.assertEqual(expected, actual)

    def test_basket_with_None(self):
        basket = None
        expected = 0

        actual = ShopAssistance.calculate_total_price(basket)

        self.assertEqual(expected, actual)

    def test_basket_with_products_positive(self):
        product1 = Product(5)
        product2 = Product(10)
        product3 = Product(3)

        basket = Basket()
        basket.add(product1)
        basket.add(product2)
        basket.add(product3)

        expected = 18

        actual = ShopAssistance.calculate_total_price(basket)

        self.assertEqual(expected, actual)

    def test_basket_with_one_positive(self):
        product = Product(5)

        basket = Basket()
        basket.add(product)

        expected = product.price

        actual = ShopAssistance.calculate_total_price(basket)

        self.assertEqual(expected, actual)





if __name__ == "__main__":
    unittest.main()
