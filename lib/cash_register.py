#!/usr/bin/env python3

class CashRegister:
  def  __init__(self,discount=0):
    self.total= 0
    self.discount = discount
    self.items = []
    self.last_transaction = 0
    
  def add_item(self,item_name,price,quantity=1):
    transaction_total = price * quantity
    self.total += transaction_total
    self.last_transaction_amount = transaction_total
    for _ in range(quantity):
     self.items.append(item_name)

  def apply_discount(self):
    if self.discount >0:
        discounted_total = self.total - (self.total * (self.discount / 100))
        self.total = discounted_total
        print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
  def void_last_transaction(self):
    self.total -= self.last_transaction_amount

cash_register = CashRegister(5)
cash_register.add_item("Book",300,2)
cash_register.add_item("Lucky Charms", 200,2)
print(cash_register.total)
cash_register.apply_discount()
print(cash_register.total)
print(cash_register.items)
cash_register.void_last_transaction()
print(cash_register.total)


    
