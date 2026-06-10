from inventory_app.models import *
from inventory_app.handlers import (
    load_config,
    demonstrate_reraise
)
from inventory_app.utils.formatter import format_inventory


def main() -> None:

    print("=== Завдання 1 ===")

    try:
        int("abc")

    except ValueError:
        print("Перехоплено ValueError")

    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            file.read()

    except FileNotFoundError:
        print("Файл не знайдено")

    else:
        print("Файл успішно відкрито")

    finally:
        print("finally виконано")

    try:
        value = int("text")
        print(10 / value)

    except (ValueError, ZeroDivisionError):
        print("Перехоплено кілька типів виключень")

    print("\n=== Завдання 2 ===")

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

    print("\n=== Завдання 3 ===")

    inventory.add_product("Laptop", 10)

    print(format_inventory(
        inventory.get_products()
    ))

    print("Перевірка __all__:")
    print(Inventory)

    print("\n=== Завдання 4 ===")

    print(Inventory.__doc__)
    print(Inventory.__name__)
    print(Inventory.add_product.__annotations__)

    help(Inventory)


if __name__ == "__main__":
    main()