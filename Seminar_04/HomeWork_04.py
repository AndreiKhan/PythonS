# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint

# задаем началльные данные
k = 3
numbers = [2, 6, 1, 9]

# метод по созданию файла и записи его в файл
def polynomial(listNumbers, ko):

    line = None
    
    # работаем с файлом, если его нет, то создадим, а если он есть то перезапишем его
    with open('file.txt', 'w') as data:

        data.writelines(str(listNumbers) + '\n')

        # проходимся по списку
        for i in listNumbers:

            # строка будет равна нужному выражению
            line = str(i) + 'x^' + str(ko) + ' + '

            # если элемент списка последний и предпоследний то изменяем строку на нужное
            if listNumbers.index(i) == len(listNumbers) - 2:
                line = str(i) + 'x + '
            if listNumbers.index(i) == len(listNumbers) - 1:
                line = str(i) + ' = 0'
            
            # записываем нужное выражение в файл
            data.write(line)
            ko -= 1


polynomial(numbers, k)




# или так _______

def create_formula(factors):
    k = len(factors) - 1
    res = ""

    for i in range(0, len(factors)):

        if i == len(factors) - 1:
            res += f"{factors[i]}"

        elif k == 1:
            res += f"{factors[i]}x + "

        else:
            res += f"{factors[i]}x^{k} + "

        k -= 1
    
    return res

print(create_formula([2, 3, 4]))

def polinome(k, file_name):
    factors = [randint(1, 101) for _ in range(0, k + 1)]
    res = create_formula(factors)

    with open(file_name, "w", encoding="UTF-8") as f:
        f.write(' '.join([str(i) for i in factors[::-1]]) + '\n')
        f.write(res)

polinome(3, 'file1.txt')
polinome(3, 'file2.txt')