# Напишите программу, удаляющую из текста все слова, содержащие "абв".


# задаем список
words = ['ПРИВЕТ', 'ЗАБВЕНИЕ', 'ПОКА']

# удаляем элементы содержащие абв
filt = filter(lambda x: not 'абв' in x.lower() , words)

print(list(filt))