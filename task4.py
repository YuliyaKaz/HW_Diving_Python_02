# Задача 4. Сумма и произведение дробей
# Программа принимает две строки вида "a/b" - дробь с числителем и
# знаменателем. Возвращает сумму и произведение дробей. Для проверки
# используется модуль fractions

from fractions import Fraction

# парсит значение числителя и знаминателя
def parse_function(func_str):
    try:
        numerator, denominator = map(int, func_str.split("/"))
        return numerator, denominator
    except(ValueError, AttributeError):
        raise ValueError("Некорректный формат числа")


def compute_sum_and_pruduct(fr1, fr2):
    a, b = parse_function(fr1)
    c, d = parse_function(fr2)

    sum_num = a * d + c * b
    sum_denum = b * d

    product_num = a*c
    product_denum = b*d

    # сокращение дробей по методу Эвклида
    def gcd(x,y):
        while y:
            x, y = y, x % y
        return x

    # сокращаем дробь суммы
    gcd_sum = gcd(sum_num, sum_denum)
    simplified_sum = f"{sum_num // gcd_sum}/{sum_denum // gcd_sum}"

    # сокращаем дробь произведения
    gcd_prod = gcd(product_num, product_denum)
    simplified_prod = f"{product_num // gcd_prod}/{product_denum // gcd_prod}"

    return simplified_sum, simplified_prod



# Ввод дробей от пользователя
fr1 = input("Введите первую дробь (a/b): ")
fr2 = input("Введите вторую дробь (c/d): ")

try:
    # вычисляем сумму и произведение
    sum_result, prod_result = compute_sum_and_pruduct(fr1, fr2)
    print(f"Сумма: {sum_result}")
    print(f"Произведение: {prod_result}")

    f1 = Fraction(fr1)
    f2 = Fraction(fr2)
    print("\nПроверка с помощью fractions:")
    print(f"Сумма: {f1 + f2}")
    print(f"Произведение: {f1 * f2}")

except ValueError as e:
    print(f"Ошибка: {e}")
