# Создайте программу для игры в "Крестики-нолики".


import random

# вводим начальные данные
cells = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
coin = random.randint(0, 1)
cross = ''
o = ''

# выведем поле для начала игры
print(cells[0], ' ', cells[1], ' ', cells[2])
print(cells[3], ' ', cells[4], ' ', cells[5])
print(cells[6], ' ', cells[7], ' ', cells[8])
print()

# метод для вывода поля и заполнения его крестиками и ноликами
def crosso(coin, point):

    if coin == 1:
        cells[int(point) - 1] = 'X'
    else:
        cells[int(point) - 1] = 'O'

    # выводим поле и меняем его
    print(cells[0], ' ', cells[1], ' ', cells[2])
    print(cells[3], ' ', cells[4], ' ', cells[5])
    print(cells[6], ' ', cells[7], ' ', cells[8])
    print()

    # меняем ход
    if coin == 1:
        coin = 0
    else:
        coin = 1

    return coin

#цикл для игры пока игрок не введет Y
while True:

    if coin == 1:
        print('введите    Y     если хотите закончить')
        cross = input('Куда поставить крестик ')
        print()

        if cross == 'Y':
            break

        coin = crosso(coin, cross)

    else:
        print('введите    Y     если хотите закончить')
        o = input('Куда поставить нолик ')
        print()

        if o == 'Y':
            break

        coin = crosso(coin, o)
