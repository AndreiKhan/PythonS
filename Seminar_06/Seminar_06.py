# Вводится список целых чисел в одну строчку через пробел. 
# Необходимо оставить в нем только двузначные числа. 
# Реализовать программу с использованием функции filter. 
# Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.

# lst = list(map(int, input().split()))

# print(*list(filter(lambda x: 9 < x < 100, lst)))


# # ИЛИ


# from random import shuffle


# lst = [i for i in range(1,20)]
# shuffle(lst)
# print(lst)
# lst = list(filter(lambda x: len(str(x)) == 2, lst))
# print(*lst)




# Дан список, вывести отдельно буквы и цифры.

# a = ('1', "a", 'b', '2', '3', 'c')
# b = ('a', 'b', 'c')
# c = ('1', '2', '3')
# lst = ['1', 'vb', '2', 'fg']

# print([i for i in lst if i.isdigit()])

# print([i for i in lst if i.isalpha()])


# # ИЛИ


# a = ['1', "a", 'b', '2', '3', 'c']

# b = list(filter(lambda x: x.isalpha(), a))
# c = list(filter(lambda x: x.isdigit(), a))




# Преобразовать набор списков (используя функцию zip)

# from itertools import zip_longest


# users = ['user1', 'user2', 'user3', 'user4', 'user5', ]
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]

# temp = [list(i) for i in zip_longest(users, ids, salary, fillvalue='')]

# for i in range(len(temp)):
#     temp[i] = list(filter(lambda x: x, temp[i]))

# print(temp)
# print(list(zip_longest(*temp)))




# Обработка текста
# Напишите программу для обработки текста.
# На вход вашей программы подаётся многострочный текст, причём число строк заранее неизвестно.
# Ваша задача – пронумеровать слова в нём, начиная с нуля, а затем вывести только те слова, которые начинаются с большой буквы.
# Перед словом необходимо вывести номер первого вхождения этого слова в текст.
# Слова необходимо отсортировать в лексикографическом порядке. (В решении задачи поможет функция enumerate())
# Ехал Грека через реку.
# Видит Грека в реке рак.
# Сунул в реку руку Грека.
# Рак за руку Греку цап.
# 4 - Видит
# 1 - Грека
# 17 - Греку
# 0 - Ехал
# 14 - Рак
# 9 - Сунул



text = []
dic = {}

for i in range(4):
    text.extend(input(). replace('.', '').split())

for i, k in enumerate(text):
    if k[0].isupper():
        if k not in dic:
            dic[k] = 1

for k, v in sorted(dic.items()):
    print(f'{v} - {k}')


# # ИЛИ


text = 'Ехал Грека через реку. Видит Грека в реке рак. Сунул в реку руку Грека. Рак за руку Греку цап.'

lst = list(text.split())

dic = dict(enumerate(lst))
dic2 = {}

for i in dic.keys():
    if dic[i].strip(".") not in dic2.values():
        if dic[i].istitle(): dic2[i] = dic[i]
    
print(dic2)

a = sorted(dic2.items(), key=lambda x: x[1])

print(*a)