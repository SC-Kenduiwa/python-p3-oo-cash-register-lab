#!/usr/bin/env python3

class CashRegister:
  def __init__(self):
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0  # Hint #3: Additional attribute to keep track of last transaction

  def add_item(self, item_name, price, quantity=1):
        # Add the price of the item to the total
        self.total += price * quantity
        # Record the last transaction amount
        self.last_transaction_amount = price * quantity
        # Add the item and its quantity to the list of items
        self.items.append({'name': item_name, 'price': price, 'quantity': quantity})

  def void_last_transaction(self):
        # Remove the last transaction from the total
        self.total -= self.last_transaction_amount
        # Clear the last transaction amount
        self.last_transaction_amount = 0

  def apply_discount(self, discount_percentage):
        # Apply the discount to the total
        discount_amount = self.total * (discount_percentage / 100)
        self.total -= discount_amount
        # Return the discounted total as a float
        return float(self.total)

# Test the class
register = CashRegister()
register.add_item("Apple", 1.5, 2)
register.add_item("Banana", 0.75, 4)
print(register.apply_discount(10))  # Output: 6.3
