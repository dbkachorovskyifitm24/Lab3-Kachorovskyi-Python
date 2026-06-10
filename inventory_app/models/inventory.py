from .exceptions import (
    ValidationError,
    ProductNotFoundError,
    StockError
)


class Inventory:
    """Клас складу товарів."""

    def __init__(self):
        self.products: dict[str, int] = {}

    def add_product(self, name: str, quantity: int) -> None:
        """Додає товар на склад."""

        if not name:
            raise ValidationError("name")

        if quantity < 0:
            raise ValidationError("quantity")

        self.products[name] = quantity

    def remove_product(self, name: str, quantity: int) -> None:
        """Списує товар зі складу."""

        if name not in self.products:
            raise ProductNotFoundError(name)

        if self.products[name] < quantity:
            raise StockError(name)

        self.products[name] -= quantity

    def get_products(self) -> dict[str, int]:
        """Повертає всі товари."""

        return self.products