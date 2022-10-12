# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


# открываем файлы для работы с ними и нахождения суммы
data1 = open('file.txt', 'r')
data2 = open('file2.txt', 'r')

# создаем списки и переменные в которые заносим данные из файлов
line1 = data1.readline()
line2 = data2.readline()
line3 = []
k = 0

# закрываем файлы
data1.close()
data2.close()


# метод по созданию файла и записи его в файл(берем метод из 4 задания)
def polynomial(listNumbers, ko):

    line = None
    
    # работаем с файлом, если его нет, то создадим, а если он есть то перезапишем его
    with open('file3.txt', 'w') as data:

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


# убираем лишнее из получившихся строк и получаем списки
line1 = line1[1:-2].split(', ')
line2 = line2[1:-2].split(', ')

# провереям длины списков чтобы посчитать коэф и сумму двух многочленов для выполнения задачи
if len(line1) >= len(line2):
    
    # расширяем списки дополняя их нулями
    line2.extend(['0',] * (len(line1) - len(line2)))
    k = len(line1) - 1
else:
    line1.extend(['0',] * (len(line2) - len(line1)))
    k = len(line2) - 1

# заполняем список для нахождения суммы многочленов
for i in range(0, len(line1)):
    line3.append(int(line1[i]) + int(line2[i]))

# обращаемся к методу для записи ответа в новый файл
polynomial(line3, k)




# или так _______

pol_1 = []


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


with open("file.txt") as f1, open('file2.txt') as f2:
    factors1 = [int(i) for i in f1.readline().split()]
    factors2 = [int(i) for i in f2.readline().split()]

if len(factors1) == len(factors2):
    res = [a + b for a, b in zip(factors1, factors2)]

elif len(factors1) > len(factors2):
    res = factors1.copy()

    for i in range(len(factors2)):
        res[i] += factors2[i]

else:
    res = factors2.copy()

    for i in range(len(factors1)):
        res[i] += factors1[i]

with open('file_3.txt', 'w') as f:
    f.write(create_formula(res[::-1]))
