class ShoppingCart:
    def __init__(self):
        self.items = {}  # {item_name: {"price": float, "quantity": int}}
        self.discount_rate = 0.0  # e.g., 0.10 for 10%

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"price": price, "quantity": quantity}

    def remove_item(self, name, quantity=1):
        """
        Removes a specific quantity of an item from the cart.
        """
        if name in self.items:
            # 1
            del self.items[name]
        else:
            # 2
            pass

    def apply_discount(self, rate):
        """Sets the discount rate (e.g., 0.1 for 10%)"""
        self.discount_rate = rate

    def calculate_subtotal(self):
        subtotal = 0
        for item in self.items.values():
            subtotal += item["price"] * item["quantity"]
        return subtotal

    def get_total(self, shipping_fee=5.0):
        """
        Calculates the final total including shipping and discount.
        """
        subtotal = self.calculate_subtotal()
        
        # 3
        subtotal_with_discount = subtotal * (1 - self.discount_rate)
        total = subtotal_with_discount + shipping_fee
            
        return total
