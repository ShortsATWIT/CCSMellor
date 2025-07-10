import unittest
from Lab5 import (
    get_products_sorted_by_price,
    get_customers_m_to_z,
    get_products_price_range,
    get_order_item_totals,
    get_products_with_category,
    get_addresses_for_allan,
    get_shipping_addresses
)

class TestGuitarShopQueries(unittest.TestCase):

    def test_get_products_sorted_by_price(self):
        results = get_products_sorted_by_price()
        self.assertIsInstance(results, list)
        if results:
            self.assertGreaterEqual(results[0][2], results[-1][2])  # list_price descending

    def test_get_customers_m_to_z(self):
        results = get_customers_m_to_z()
        self.assertIsInstance(results, list)
        if results:
            for row in results:
                self.assertGreaterEqual(row[1], 'M')  # last_name >= 'M'
                self.assertIn(', ', row[2])           # full_name formatted correctly

    def test_get_products_price_range(self):
        results = get_products_price_range()
        self.assertIsInstance(results, list)
        for row in results:
            self.assertGreater(row[1], 500)
            self.assertLess(row[1], 2000)

    def test_get_order_item_totals(self):
        results = get_order_item_totals()
        self.assertIsInstance(results, list)
        for row in results:
            item_total = row[6]
            self.assertGreater(item_total, 500)

    def test_get_products_with_category(self):
        results = get_products_with_category()
        self.assertIsInstance(results, list)
        if results:
            for row in results:
                self.assertIsInstance(row[0], str)  # category_name
                self.assertIsInstance(row[1], str)  # product_name
                self.assertIsInstance(row[2], float)  # list_price

    def test_get_addresses_for_allan(self):
        results = get_addresses_for_allan()
        self.assertIsInstance(results, list)
        for row in results:
            self.assertEqual(row[0], 'Allan')  # first_name
            self.assertEqual(row[1], 'Sherwood')  # last_name

    def test_get_shipping_addresses(self):
        results = get_shipping_addresses()
        self.assertIsInstance(results, list)
        for row in results:
            self.assertIsInstance(row[0], str)  # first_name
            self.assertIsInstance(row[1], str)  # last_name

if __name__ == '__main__':
    unittest.main()
