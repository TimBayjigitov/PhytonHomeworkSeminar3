# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
#   [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#   [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            num = [float(i) for i in input(inputText).split()]
            is_OK = True
        except ValueError:
            print("это не число, повторите попытку")
    return num

def Difference(list):
    list2 = []
    for i in list:
        x = i%1
        list2.append(x)
    max_value = max(list2)
    min_value = min(list2)
    diff = max_value - min_value
    return diff

ls1 = InputNumbers('Введите числа через пробел для составления списка: ')
print(round(Difference(ls1), 2))