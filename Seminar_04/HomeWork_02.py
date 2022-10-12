# Задайте натуральное число N. 
# Напишите программу, которая составит 
# список простых множителей числа N.


# получаем число
number = int(input())

# метод для получения списка простых множителей
def factor(num):
    
    # создаем список и простой множитель
    listNumbers = []
    count = 2

    # цикл для заполнения списка
    while num != 1:
        
        # если число делится без остатка то добавляем множитель в список
        if num % count == 0:
            num = num / count
            listNumbers.append(count)
        else:
            count += 1
    
    # возвращаем список
    return listNumbers

# выводим полученный список
print(factor(number))




# или так _______

def prime(number):
    res = []
    d = 2

    while d ** 2 <= number:
        if number % d == 0:
            res.append(d)
            number //= d
        else:
            d += 1
        
    if number > 1:
        res.append(number)
    
    return res

print(prime(200))