import random

# здесь сохраняется количество конфет
candy = 0

# метод для вычета конфет которые взял игрок
def player(getcandy):
    global candy

    candy -= getcandy

# метод дающий "ум" боту и вычитающий количесвто конфет которые он взял
def bot():
    global candy

    # проверка дающая боту побеждать
    if 29 < candy < 58:
        getcandy = candy - 29
        candy -= getcandy
        return getcandy

    # случайное количество конфет забирает бот
    getcandy = random.randint(1, 28)
    candy -= getcandy

    return getcandy

# метод для записи количества конфет
def game(getcandy):
    global candy
    candy = getcandy
