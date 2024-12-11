def numbers_sum():
    countNumber = int(input("Введите количество чисел: "))
    sum = 0
    for i in range(countNumber):
        num = int(input("Введите число: "))
        sum += num
    print("Сумма чисел:", sum)

numbers_sum()
