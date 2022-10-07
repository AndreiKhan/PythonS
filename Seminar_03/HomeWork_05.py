# Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.

# задаем число
input = int(input())

# метод по подсчету Фибоначчи
def fibonachi(number):
    list = []

    # получаем модуль числа если заданное число отрицательное
    count = abs(number)
    number = abs(number)

    # если заданное число равно 0 или 1, то выводим сразу нужный список с числами Фибоначчи
    if number <= 1:
        if number == 1:
            list = [1, 0, 1]
        else:
            list = [0]
    else:

        #задаем начальный список для подсчета
        list = [1, 0, 1]

        # заполняем список положительными числами Фибоначчи
        while number > 1:
            list.append(list[-1] + list[-2])
            number -= 1

        # заполняем список отрицательными числами Фибоначчи
        while count > 1:
            list.insert(0, list[1] - list[0])
            count -= 1

    #выводим результат
    print(list)


fibonachi(input)




# или так _______

n = 8
fib = [0, 1]

for i in range(2, n + 1):
    fib.append(fib[-1] + fib[-2])

for i in range(n):
    # fib = [fib[1] - fib[0]] + fib
    fib.insert(0, fib[1] - fib[0])

print(fib)