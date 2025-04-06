# Задание 2 Преобразование числа в шестнадцатеричное
# представление
# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте для
# проверки своего результата.

def int_to_hex(n):
    if n == 0:
        return 0x0

    hex_digit = "0123456789abcdef"
    is_negative = n < 0
    n = abs(n)

    hex_str=""
    while n>0:
        reminder = n % 16
        hex_str = hex_digit[reminder]+ hex_str
        n = n // 16

    if is_negative:
        hex_str = '-' + hex_str

    return "0x" + hex_str

num = int(input("Введите число: "))
custom_hex = int_to_hex(num)
builtin_hex = hex(num)

print(f"Наш результат: {custom_hex}")
print(f"Эталонный результат: {builtin_hex}")

if custom_hex == builtin_hex:
    print("✅ Результаты совпадают!")
else:
    print("❌ Результаты не совпадают!")