#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []


  def add_item(self, title, price, quanity = 1):
    self.total += (price * quanity)

    for i in range(quanity):
      self.items.append(title)

    self.last_transcation = {
      "price": price,
      "quantity": quanity
    }

  def apply_discount(self):
    if self.discount > 0:
      discount_amount = (self.discount / 100) * self.total
      self.total -= discount_amount
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= (self.last_transcation['price'] * self.last_transcation['quantity'])

    for i in range(self.last_transcation['quantity']):
      self.items.pop()
                   
    
      
  
