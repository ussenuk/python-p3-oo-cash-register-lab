#!/usr/bin/env python3


class CashRegister:

  def __init__(self, discount = 0):
    
    # Assign to self object
    
    self.discount = discount
    self.total = 0
    self.items = []
    self.track_subtotal = []
 
  
  def add_item(self, title, price, quantity=1):
      self.title = title
      self.price = price
      self.quantity = quantity 
      
      self.total += quantity*price
      
      self.track_subtotal.append(price*quantity)

      # you should append the title to the items list quantity number of times.
      # This way, each item gets appended to the items list individually, even when multiple quantities of the same item are added. 
      for _ in range(quantity):
        self.items.append(title)

      return self.total
  
  
  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
      # return self.total
    else:
      self.total = self.total * (1-(self.discount/100))
      print(f"After the discount, the total comes to ${int(self.total)}.")
      return self.total
    
  def void_last_transaction(self):
    self.total -= self.track_subtotal[-1]
    return self.total

# without discount
    
# cash_register = CashRegister()
# cash_register.add_item("Books",5.00, 3)
# cash_register.apply_discount()
# cash_register.add_item("Ritz Crackers", 5.0)
# cash_register.add_item("Justin's Peanut Butter Cups", 2.50, 2)


# with discount

# cash_register_with_discount = CashRegister(discount = 20)
# cash_register_with_discount.add_item("macbook air", 1000)
# print(cash_register_with_discount.total)
# cash_register_with_discount.apply_discount()
# print(cash_register_with_discount.total)



# returning array 

new_register = CashRegister()
new_register.add_item("eggs", 1.99, 2)
new_register.add_item("tomato", 1.76, 3)
print(new_register.items)
    
# void transaction

# cash_register = CashRegister()
# cash_register.add_item("apple", 0.99)
# cash_register.add_item("tomato", 1.76)
# print(cash_register.total)
# cash_register.void_last_transaction()
# print(cash_register.total)
