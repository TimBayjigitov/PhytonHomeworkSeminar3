# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
import math

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            num = [int(i) for i in input(inputText).split()]
            is_OK = True
        except ValueError:
            print("это не число, повторите попытку")
    return num

def FindHalfIndex(list):
    half_index = 0
    count_index = 0
    for i in list:
        count_index+=1
    half_index = math.ceil(count_index/2)
    return half_index

def MultDigitofList(list1,list2):
    list3 = []
    proiz = 1
    for i in list1:
        for j in list2:
            if list1.index(i)==list2.index(j):
                proiz = i*j
                list3.append(proiz)
    return list3

ls1 = InputNumbers('Введите числа через пробел для составления списка: ')
ls2 = ls1[::-1]

ls1 = ls1[:FindHalfIndex(ls2)]
ls2 = ls2[:FindHalfIndex(ls2)]
print(MultDigitofList(ls1,ls2))
