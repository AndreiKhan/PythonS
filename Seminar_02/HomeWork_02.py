# Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.

number = int(input())
count = 1
listOfNumbers = list()

# Цикл для заполнения списка числами
while len(listOfNumbers) < number:

    # Добавляем в список число
    listOfNumbers.append(count)

    # Считаем следующее число
    count *= (len(listOfNumbers) + 1)

# Выводим ответ как в примере
print(listOfNumbers)
