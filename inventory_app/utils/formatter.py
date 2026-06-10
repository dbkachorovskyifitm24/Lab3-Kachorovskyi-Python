def format_inventory(products: dict[str, int]) -> str:
    """Форматує список товарів."""

    result = "\nСклад:\n"

    for name, quantity in products.items():
        result += f"{name}: {quantity}\n"

    return result