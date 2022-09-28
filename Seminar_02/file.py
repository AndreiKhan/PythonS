import random

def randomPosition(list):
    number = list[random.randint(0, len(list) - 1)] * list[random.randint(0, len(list) - 1)]
    return number