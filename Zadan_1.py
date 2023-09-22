import random

sum = 0
#a = random.randint(0,99999)
while True:
    try:
        a=int(input("Введите число: "))
        break
    except ValueError:
        print("Ошибка!")
print(a)
while a > 0:
    if a % 10 % 2 == 1:
        sum += a % 10
    a = a // 10
print("Суммма всех нечетных цифр числа равна ", sum)