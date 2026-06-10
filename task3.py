from inventory_app.models import *
from inventory_app.utils.formatter import format_inventory

inventory = Inventory()

inventory.add_product("Laptop", 10)
inventory.add_product("Mouse", 15)

print(format_inventory(
    inventory.get_products()
))

print(Inventory)