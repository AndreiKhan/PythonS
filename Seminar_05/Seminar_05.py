# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найдите это число.


# list = [int(i) for i in input('через пробел ').split()]

# print(list)

# for i in range(len(list) - 1):
#     if list[i + 1] - list[i] != 1:
#         print(list[i] + 1)




# Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.
# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.


# nums = [i for i in range(10, 101)]

# res = sum(map(lambda x: x ** 2, filter(lambda x: not x % 9, nums)))

# print(res)




# Напишите функцию triangle(a, b, c), которая принимает на вход 
# три длины отрезков и определяет, можно ли из этих отрезков составить треугольник.


# a = int(input())
# b = int(input())
# c = int(input())

# def triangle(a, b, c):
#     flag = False

#     if (a + b) > c and (a + c) > b and (b + c) > a:
#         flag = True

#     return 'yes' if flag else 'no'

# print(triangle(a, b, c))




# Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.


list = [1, 5, 2, 3, 4, 6, 1, 7]
list_res = []

for j in range(1, len(list)):
    list_temp = [list[0]]

    for i in range(j, len(list)):

        if list[i] >= list_temp[-1]:
            list_temp.append(list[i])
    
    list_res.append(list_temp)

print(list_res)
