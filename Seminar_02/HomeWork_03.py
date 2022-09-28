# Задайте список из n чисел последовательности (1 + (1 / n)) ** n 
# выведите на экран их сумму.

number = int(input())
listOfNumbers = list()

# Цикл для подсчета последовательности чисел от 1 до number
while number > 0:

    # Добавляем в список число
    listOfNumbers.append((1 + 1 / number) ** number)

    # Уменьшаем полученное число до 0
    number -= 1

# Проходимся по всему списку и считаем сумму
for i in listOfNumbers:
    
    number += i

# Выводим на экран
print(listOfNumbers)
print(round(number, 2))
