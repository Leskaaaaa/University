#Task1.1
def filter_numbers_in_range(numbers, start=1, end=3):
    return [num for num in numbers if start <= num <= end]

numbers = [0, 2, 5]

filtered_numbers = filter_numbers_in_range(numbers)
print(filtered_numbers)

#Task1.2
def check_same_digits(number):
    if 10 <= abs(number) <= 99:
        digits = str(number)
        if digits[0] == digits[1]:
            return "Да"
        else:
            return "Нет"
    else:
        return "Число не является двузначным"

number = int(input("Введите двузначное число: "))
result = check_same_digits(number)
print(result)

# Task3
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Введите число для проверки на простоту: "))

if is_prime(number):
    print("Число простое")
else:
    print("Число не является простым")