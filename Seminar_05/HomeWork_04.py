# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


text = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'

# метод для шифрования текста
def rle(text):

    cod = []
    count = 0
    words = 1

    # проходимся по тексту пока он не станет пустым
    while text != '':

        # если остался последний символ то мы добавляем его и выходим из цикла
        if len(text) == 1:

            cod.append([text[0], words])

            break

        while text[0] == text[1]:

            words += 1

            # убираем первый символ текста
            text = text[1:]

            # если остался последний символ то мы выходим из цикла
            if len(text) == 1:
                break
        
        # добавляем в список зашифрованные символы
        cod.append([text[0], words])
        
        # меняем итераторы
        count += 1
        words = 1
        
        # убираем первый символ текста
        text = text[1:]

    return cod

def decode(code):

    decodeText = ''

    # проходимся по шифрованному тексту
    for i in range(0, len(code)):

        # выводим получившийся текст после дешифровки
        decodeText += code[i][0] * code[i][1]

    return decodeText

# кодируем текст
codeText = rle(text)
print(codeText)

# декодируем текс
decodeText = decode(codeText)
print(decodeText)
