# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.


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
