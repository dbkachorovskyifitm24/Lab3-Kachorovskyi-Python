import json

from inventory_app.models.exceptions import InventoryError
from inventory_app.utils.logger import log


def load_config(filename: str) -> dict:
    """Завантаження конфігурації."""

    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError as error:
        raise InventoryError(
            "Файл конфігурації не знайдено"
        ) from error


def demonstrate_reraise() -> None:
    """Повторне піднесення виключення."""

    try:
        raise InventoryError("Тестове виключення")

    except InventoryError:
        log("Виключення записано до журналу")
        raise