# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            num = [int(i) for i in input(inputText).split()]
            is_OK = True
        except ValueError:
            print("это не число, повторите попытку")
    return num

def FindSumOddNumber(list):
    index = 0
    suma = 0
    for i in list:
        if index % 2 !=0:
            suma +=i
        index +=1
    return suma
data = list(InputNumbers('Введите числа через пробел для составления списка: '))
print(f'Сумма нечетных позиций в списке равно = {FindSumOddNumber(data)}')

