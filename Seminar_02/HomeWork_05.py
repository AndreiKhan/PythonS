# Реализуйте алгоритм перемешивания списка.

import random

list = [1, 'a', True, 2, 'b', False]

# Метод премешивания с помощью shuffle
def shuf(list):

    random.shuffle(list)

    return list

# Метод премешивания с помощью randint
def randin(list):

    count = 0

    while count != len(list) - 1:

        # Записываем индексы и переменную для использования
        n1 = random.randint(0, len(list) - 1)
        n2 = random.randint(0, len(list) - 1)
        n3 = list[n1]

        # Перемешиваем элементы списка
        list[n1] = list[n2]
        list[n2] = n3

        count += 1

    return list

# Метод премешивания с помощью choice
def choic(list):

    count = 0

    while count != len(list) - 1:

        # Записываем индексы и переменную для использования
        n1 = list.index(random.choice(list))
        n2 = list.index(random.choice(list))
        n3 = list[n1]

        # Перемешиваем элементы списка
        list[n1] = list[n2]
        list[n2] = n3

        count += 1

    return list

print(shuf(list))
print(randin(list))
print(choic(list))
