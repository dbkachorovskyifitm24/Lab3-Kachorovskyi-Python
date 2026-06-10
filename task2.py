from inventory_app.models import (
    Inventory,
    InventoryError,
    ValidationError
)

from inventory_app.handlers.command_handler import (
    load_config,
    demonstrate_reraise
)

inventory = Inventory()

try:
    inventory.add_product("Laptop", -5)

except ValidationError as error:
    print(error)

try:
    load_config("missing.json")

except InventoryError as error:
    print(error)

    if error.__cause__:
        print("Причина:", error.__cause__)

try:
    demonstrate_reraise()

except InventoryError as error:
    print(error)