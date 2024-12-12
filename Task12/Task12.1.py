def sum_of_digits_recursive(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits_recursive(n // 10)

n = int(input("Введите натуральное число N: "))
if n <= 0:
    print("Ошибка: введите натуральное число больше 0")
else:
    result = sum_of_digits_recursive(n)
    print(f"Сумма цифр числа {n} равна {result}.")