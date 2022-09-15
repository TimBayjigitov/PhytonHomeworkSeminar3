# # 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# # Пример:
# # для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            num = int(input(inputText))
            if num < 0:
                print("Введите положительное число: ")    
            else:
                is_OK = True
        except ValueError:
            print("Это не является числом")
    return num

def FibbonaciRight(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else: return FibbonaciRight(num-2) + FibbonaciRight(num-1)

def FibbonaciLeft(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else: return FibbonaciLeft(num-2) - FibbonaciLeft(num-1)
            

Positive_List = []
Negative_List = []
number = InputNumbers('Введите число: ')
for i in range(number+1):
    Positive_List.append(FibbonaciRight(i))

for i in range(1,number+1):
    Negative_List.append(FibbonaciLeft(i))
print(Negative_List[::-1] + Positive_List)

