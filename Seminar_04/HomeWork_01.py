# Вычислить число c заданной точностью d


from math import pi

# пусть d = 0.001
d = 0.001
p = pi

# метод для округления числа
# numb - число которое надо округлить
# roun - число для определения сколько нужно цифр после запятой
def roundNum(numb, roun):

    # счетчик для определения сколько цифр после запятой
    count = 0

    while roun != 1:
        roun *= 10
        count += 1

    # используем функцию для округления и получаем нужное число с точностью d
    numb = round(numb, count)

    return numb

# обращаемся к методу и получаем нужное число
p = roundNum(p, d)
print(p)




# или так _______

def my_round(n, d):
    return round(n, d)

d = 0.0001
print(my_round(p, str(d).count('0')))
