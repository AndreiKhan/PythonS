# -----1 задача-----
# Даны три целых числа. Определите, сколько среди них совпадающих. 
# Программа должна вывести одно из чисел: 3 , 2  или 0

# a, b, c = int(input()), int(input()), int(input())

# if a == b == c:
#     print(3)
# elif a == b or a == c or b == c:
#     print(2)
# else:
#     print(0)

# -----2 задача-----
# Даны два целых числа A и В, A>BA>B. Выведите все нечётные числа
# от A до B включительно, в порядке убывания. В этой задаче можно обойтись без инструкции if.

# a = int(input())
# b = int(input())

# for i in range(a - (a + 1) % 2, b - 1, 2):
#     print(i, end = ' ')

# -----3 задача-----
# Напишите программу, которая принимает на вход число N 
# и выдаёт последовательность из N членов.

# n = 5
# for i in range(0, n):
#     print((-3) ** i)

# -----4 задача-----
# Напишите программу, которая проверяет пятизначное число на палиндром.

# number = "123215"
# palindrome = True

# for i in range(len(number) // 2):
#     if number[i] != number[-i - 1]:
#         palindrome = False
#         break

# if palindrome:
#     print("Палиндром")
# else:
#     print("Не палиндром")

# # Второй вариант

# number = "12321"
# print(number == number[::-1])

# -----5 задача-----
# Удалить вторую цифру трёхзначного числа.

# number = 546
# n1 = number // 100
# n2 = number % 10
# res = n1 * 10 + n2
# print(res)

# Второй вариант

# number = "546"
# print(number[0] + number[2])

# Третий вариант

# number = list(str(123))
# del number[1]
# print(''.join(number))

# -----6 задача-----
# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

# string = "cccchjkccc"
# find = "cc"
# count = 0
# i = 0
# while i < len(string):
#     if string[i : i + len(find)] == find:
#         count += 1
#         i += len(find)
#     else:
#         i += 1
# print(count)

# доп задача №1
# По данному целому числу N распечатайте все квадраты натуральных чисел,
# не превосходящие N, в порядке возрастания.

# number = int(input())
# count = 1

# while number >= count ** 2:
#     print(count ** 2)
#     count += 1
