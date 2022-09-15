# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            num = int(input(inputText))
            is_OK = True
        except ValueError:
            print("это не число, повторите попытку")
    return num


def ConvertToBinary(num):
    a = 0
    ls = []
    while num != 0:
        a = num % 2
        ls.append(a)
        num //= 2
        ConvertToBinary(num)
    return reversed(ls)

n = InputNumbers('Введите число: ')

print(list(ConvertToBinary(n)))