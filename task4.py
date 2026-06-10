from inventory_app.models.inventory import Inventory

print("DOCSTRING:")
print(Inventory.__doc__)

print("\nNAME:")
print(Inventory.__name__)

print("\nANNOTATIONS:")
print(Inventory.add_product.__annotations__)

print("\nHELP:")
help(Inventory)