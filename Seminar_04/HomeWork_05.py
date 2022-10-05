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
