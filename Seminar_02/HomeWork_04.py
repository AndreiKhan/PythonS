# Задайте числами список из N элементов, заполненных из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# # Первый вариант через файл file.txt
# # ------------------------------------------------------------

import random

number = int(input())

listOfNumbers = list()
listOfMulti = list()
listOfPositions = list()

# Открываем файл file.txt
position = open('file.txt')

count = abs(number)

# Заполняем список по заданию
for i in range(-number, number + 1):
    listOfNumbers.append(i)

# Читаем строки в открытом файле вытаскиваем число и заносим его в список
for line in position:
    for i in line:
        if i.isdigit():
            listOfPositions.append(i)

# Цикл для подсчета чисел, берем случайную позицию которую взяли из файла и умножаем так же на случайную позицию из файла
while count != 0:

    # Умножаем два случайных числа
    number = int(listOfPositions[random.randint(0, 5)]) * int(listOfPositions[random.randint(0, 5)])

    # Добавляем его в список
    listOfMulti.append(number)

    # Повторяем операцию number число раз, т.е. если было введено число 5 то умножать случайные числа будем 5 раз
    count -= 1

# Выводим на экран
print(listOfNumbers)
print(listOfMulti)

# Закрываем файл
position.close()

# ------------------------------------------------------------


# Второй вариант через собственный модуль file.py
# ------------------------------------------------------------

# import file

# number = int(input())

# listOfNumbers = list()
# listOfMulti = list()

# count = abs(number)

# # Заполняем список по заданию
# for i in range(-number, number + 1):
#     listOfNumbers.append(i)

# # Цикл для подсчета чисел
# while count != 0:

#     # Умножаем два случайных числа обратившись к стороннему собственному модулю
#     number = file.randomPosition(listOfNumbers)

#     # Добавляем его в список
#     listOfMulti.append(number)

#     # Повторяем операцию number число раз, т.е. если было введено число 5 то умножать случайные числа будем 5 раз
#     count -= 1

# Выводим на экран
# print(listOfNumbers)
# print(listOfMulti)

# ------------------------------------------------------------
