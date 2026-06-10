try:
    int("abc")

except ValueError:
    print("Перехоплено ValueError")


try:
    with open("data.txt", "r", encoding="utf-8") as file:
        content = file.read()

except FileNotFoundError:
    print("Файл не знайдено")

else:
    print("Файл успішно прочитано")

finally:
    print("finally виконано")


try:
    value = int("text")
    print(10 / value)

except (ValueError, ZeroDivisionError):
    print("Перехоплено кілька типів виключень")