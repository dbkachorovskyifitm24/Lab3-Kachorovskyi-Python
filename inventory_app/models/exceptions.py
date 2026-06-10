class InventoryError(Exception):
    """Базове виключення системи."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return f"InventoryError: {self.message}"


class ValidationError(InventoryError):
    """Помилка валідації."""

    def __init__(self, field_name: str):
        self.field_name = field_name
        super().__init__(f"Некоректне поле: {field_name}")

    def __str__(self) -> str:
        return f"ValidationError: поле '{self.field_name}' містить некоректне значення"


class ProductNotFoundError(InventoryError):
    """Товар не знайдено."""

    def __init__(self, product_name: str):
        self.product_name = product_name
        super().__init__(f"Товар '{product_name}' не знайдено")

    def __str__(self) -> str:
        return f"ProductNotFoundError: товар '{self.product_name}' не існує"


class StockError(InventoryError):
    """Недостатньо товару."""

    def __init__(self, product_name: str):
        self.product_name = product_name
        super().__init__("Недостатня кількість товару")

    def __str__(self) -> str:
        return f"StockError: недостатньо товару '{self.product_name}'"