from item import Item
from phone import Phone
from kboard import Keyboard

# item1 = Item("MyItem", 750, 6)
# item1 = Phone("jcsPhone", 1000, 3)
# # item1.apply_increment(0.2)
# item1.apply_discount()

item1 = Keyboard("jcsKeyboard", 200, 3)

# item1.apply_increment(0.2)
item1.apply_discount()

print(item1.price)

# item1.apply_increment(0.2)
# item1.apply_discount()

# item1.send_email()
# item1.__connect()

# # Setting an Attribute
# item1.name = "OtherItemmm"

# # Getting an Attribute
# print(item1.name)
# print(Item.all)