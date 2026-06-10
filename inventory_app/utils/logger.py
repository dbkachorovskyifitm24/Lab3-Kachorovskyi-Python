from datetime import datetime


def log(message: str) -> None:
    """Логування повідомлень."""

    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")