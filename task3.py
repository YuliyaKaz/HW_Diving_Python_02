# Задача 3. Перевод целого числа в римское число
# Программа принимает целое число и возвращает его римское представление в
# виде строки

def int_to_roman(n):
    if not 1 <= n <= 3999:
        return "Число должно быть от 1 до 3999"

    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5,4,1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    roman = ""
    i = 0
    while n > 0:
        for _ in range(n//val[i]):
            roman += syms[i]
            n -= val[i]
        i+=1
    return roman

try:
    num = int(input("Введите число: "))
    print(f"Римское представление: {int_to_roman(num)}")
except ValueError:
    print("Ошибка обработки числа")
