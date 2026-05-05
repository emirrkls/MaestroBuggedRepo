import unittest
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_calculate_total_with_discount(self):
        self.cart.add_item("Laptop", 100, 1)
        self.cart.apply_discount(0.10)
        total = self.cart.get_total(shipping_fee=10.0)
        self.assertEqual(total, 100.0, "Total should be (Subtotal * Discount) + Shipping")

    def test_remove_partial_quantity(self):
        self.cart.add_item("Apple", 1.0, 3)
        self.cart.remove_item("Apple", 1)
        self.assertEqual(self.cart.items["Apple"]["quantity"], 2, "Should have 2 apples left after removing 1")

    def test_empty_cart_total(self):
        total = self.cart.get_total(shipping_fee=5.0)
        self.assertEqual(total, 0.0, "Empty cart total should be 0.0")

if __name__ == "__main__":
    unittest.main()
