# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.


# Задаем список
# list1 = [int(i) for i in input('через пробел ').split()]
list = [1.1, 1.2, 3.1, 5, 10.01]


# Создаем метод для нахождения дробной части
def minMax(list):
    min = 1
    max = 0

    # в цикле убираем целаю часть
    for i in range(0, len(list)):
        list[i] = list[i] - list[i] // 1

    # находим самую большую и меньшую дробную часть
    for i in list:
        if i > max:
            max = i
        if i < min and i != 0:
            min = i
    
    # считаем их и выводи
    print(round(max - min, 2))


minMax(list)