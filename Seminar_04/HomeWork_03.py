# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

# задаем случайный список
listNumbers = [1, 2, 2, 3, 4, 4, 0, 5, 8, 7, 7]

# или сами создаем свой список
# list1 = [int(i) for i in input('через пробел элем цифры ').split()]

# метод для создания списка с уникальными элементами из заданного списка
def unikList(numbers):
    
    unikNumbers = []

    # проходим по списку и добавляем в новый список уникальные элементы
    for i in numbers:
        if numbers.count(i) == 1:
            unikNumbers.append(i)
    
    return unikNumbers


print(unikList(listNumbers))




# или так _______

sp = [1, 2, 3, 3, 4, 2, 4]

res = [i for i in sp if sp.count(i) == 1]