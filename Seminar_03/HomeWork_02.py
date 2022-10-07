# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


# Задаем список
# list1 = [int(i) for i in input('через пробел ').split()]
list = [2, 3, 4, 5, 6]


# Создаем метод по умножению чисел парами
def countPair(list):
    
    # счетчик для подсчета количества пар в списке
    l = len(list) // 2
    countList = []

    # если список нечетный то увеличиваем счетчик для подсчета пар
    if len(list) % 2 == 1:
        l += 1

    # проходимся по списку
    for i in range(0, l):
        countList.append(list[i] * list[-(i + 1)])

    return countList


# выводим список с посчитанными парами
print(countPair(list))



# или так _______

spsk = [2, 3, 4, 5, 6]

def pair_number(lst):

    sqrt = []

    for i in range((len(lst) + 1) // 2):
        sqrt.append(lst[i] * lst[len(lst) - 1 - i])
    
    return sqrt

print(pair_number(spsk))