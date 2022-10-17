import csv

# метод для записи всех контактов из книжки
def read_contacts():
    contact = []

    # открываем txt и записываем все контакты
    with open('phone_book.txt', 'r', encoding="utf-8") as p:

        for line in p:
            contact.append(line.rstrip())

    # открываем csv и записываем все контакты
    with open("book_phone.csv", encoding='utf-8') as p:
        count = 0
        reader = csv.reader(p, delimiter = ',')

        for row in reader:
            # условие для того чтобы не записать заголовок файла
            if count != 0:
                contact.append(row[0])
                contact.append(row[1])
                contact.append(row[2])
                contact.append(row[3])
            count += 1

    return contact

# метод экспорта контакта в файл с нужным названием и форматом
def export_contact(book, contact, file):
    
    # меняем значение для вывода нужного контакта
    contact = (contact - 1) * 4

    # условие если надо вывести в txt формате
    if file[-3:] == 'txt':

        with open(file, 'w', encoding='utf-8') as f:

            for i in range(contact, contact + 4):
                f.writelines(book[i] + '\n')

    # условие если надо вывести в csv формате
    if file[-3:] == 'csv':

        with open(file, mode = "w", encoding='utf-8') as p:

            head = ['Имя', 'Фамилия', 'Телефон', 'Описание']

            writer = csv.DictWriter(p, delimiter = ",", lineterminator = "\r", fieldnames = head)
            writer.writeheader()
            writer.writerow({'Имя': book[contact], 'Фамилия': book[contact + 1], 'Телефон': book[contact + 2], 'Описание': book[contact + 3]})
    
    # выводим сообщение какой контакт был экспортирован и в какой файл
    print(f'Копия контакта "{book[contact]} {book[contact + 1]} {book[contact + 2]} {book[contact + 3]}" экспортирована в {file}')

# метод для импорта контакта/контактов в нашу книжку
def import_contact(file):
    new_contact = []

    # если контакт/контакты находятся в файле txt формата
    if file[-3:] == 'txt':

        # открываем файл в котором записаны контакты и записываем их в список
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                new_contact.append(line.rstrip())

        # открываем книжку и дописываем в нее новые контакты
        # из txt записываем в csv книжку для разнообразия
        with open('book_phone.csv', mode = "a", encoding='utf-8') as p:

            head = ['Имя', 'Фамилия', 'Телефон', 'Описание']

            writer = csv.DictWriter(p, delimiter = ",", lineterminator = "\r", fieldnames = head)

            for i in range(0, len(new_contact), 4):
                writer.writerow({'Имя': new_contact[i], 'Фамилия': new_contact[i + 1], 'Телефон': new_contact[i + 2], 'Описание': new_contact[i + 3]})

    # если контакт/контакты находятся в файле txt формата
    if file[-3:] == 'csv':

        # открываем файл в котором записаны контакты и записываем их в список
        with open(file, encoding='utf-8') as f:

            reader = csv.reader(f, delimiter = ',')

            for row in reader:
                new_contact.append(row[0])
                new_contact.append(row[1])
                new_contact.append(row[2])
                new_contact.append(row[3])

        # открываем книжку и дописываем в нее новые контакты
        # из csv записываем в txt книжку для разнообразия
        with open('phone_book.txt', 'a', encoding='utf-8') as p:
            for i in new_contact:
                p.writelines(i + '\n')

    # выводим сообщение какие контакты были добавлены
    for i in range(0, len(new_contact), 4):
        print(f'Контакт "{new_contact[i]} {new_contact[i + 1]} {new_contact[i + 2]} {new_contact[i + 3]}" добавлен в книжку')
