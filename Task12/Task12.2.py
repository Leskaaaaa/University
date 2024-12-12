def is_prime_recursive(n, divisor=2):
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime_recursive(n, divisor + 1)

n = int(input("Введите натуральное число n > 1: "))
if n <= 1:
    print("Ошибка: введите число больше 1.")
else:
    if is_prime_recursive(n):
        print("YES")
    else:
        print("NO")