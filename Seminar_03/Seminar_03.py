# Дан список. Выведите те его элементы, которые встречаются в списке только один раз. 
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

# list1 = [int(i) for i in input('через пробел элем цифры ').split()]

# list2 = list(map(int, input('через пробел элем цифры ').split()))

# for i in list:
#     if list.count(i) == 1:
#         print(i)



# Дан список чисел. Выведите все элементы списка, 
# которые больше предыдущего элемента.

# list = [int(i) for i in input("Введите числа через пробел: ").split()]

# for i in range(0, len(list) - 1):
#     if list[i] < list[i + 1]:
#         print(list[i + 1])



# Реализуйте алгоритм задания случайных чисел без использования
# встроенного генератора псевдослучайных чисел.

# from datetime import datetime


# def num_number(n):
#     number = datetime.now().microsecond
#     return number % n

# print(num_number(100))


# Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

# list = ['13', 'Строка1', 'Строка2', 'Строка3', 'Строка45', 'Стр12ка']
# a = '12'
# count = 0

# for word in list:
#     if a in word:
#         count += 1

# print('Да') if count > 0 else print('Нет')

# Напишите программу, которая определит позицию 
# второго вхождения строки в списке либо сообщит, что её нет.

# list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# list2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# list3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# list4 = ["123", "234", 123, "567"]
# list5 = []

# find1 = input()
# find2 = input()
# find3 = input()
# find4 = input()
# find5 = input()

# def ifin(list, find):
#     count = 0
#     k = 0

#     for i in list:
#         k += 1
#         if i == find:
#             count += 1
#             if count == 2:
#                 print(k - 1)

#     if count < 2:
#         print('-1')

# ifin(list1, find1)
# ifin(list2, find2)
# ifin(list3, find3)
# ifin(list4, find4)
# ifin(list5, find5)
