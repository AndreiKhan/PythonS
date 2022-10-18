import csv

# метод для записи всех контактов из книжки
def read_contacts():
    contact = []

    # открываем csv и записываем все контакты
    with open("book_people.csv", encoding='utf-8') as p:
        reader = csv.reader(p, delimiter = ',')
        head = next(reader)

        for row in reader:
            contact.append(row)

    return contact

# метод экспорта контакта в файл с нужным названием и форматом
def export_contact(book, contact, file):

    with open(file, mode = "w", encoding='utf-8') as p:

        head = ['Имя', 'Фамилия', 'Телефон', 'Описание']

        writer = csv.DictWriter(p, delimiter = ",", lineterminator = "\r", fieldnames = head)
        writer.writeheader()
        writer.writerow({'Имя': book[contact][0], 'Фамилия': book[contact][1], 'Телефон': book[contact][2], 'Описание': book[contact][3]})

    # выводим сообщение какой контакт был экспортирован и в какой файл
    print(f'Копия контакта "{book[contact][0]} {book[contact][1]} {book[contact][2]} {book[contact][3]}" экспортирована в {file}')

# метод для импорта контакта/контактов в нашу книжку
def import_contact(file):
    new_contact = []

    # открываем файл в котором записаны контакты и записываем их в список
    with open(file, encoding='utf-8') as f:

        reader = csv.reader(f, delimiter = ',')

        for row in reader:
            new_contact.append(row[0])
            new_contact.append(row[1])
            new_contact.append(row[2])
            new_contact.append(row[3])

    # открываем книжку и дописываем в нее новые контакты
    with open('book_people.csv', mode = "a", encoding='utf-8') as p:

        head = ['Имя', 'Фамилия', 'Телефон', 'Описание']

        writer = csv.DictWriter(p, delimiter = ",", lineterminator = "\r", fieldnames = head)

        for i in range(0, len(new_contact), 4):
            writer.writerow({'Имя': new_contact[i], 'Фамилия': new_contact[i + 1], 'Телефон': new_contact[i + 2], 'Описание': new_contact[i + 3]})

    # выводим сообщение какие контакты были добавлены
    for i in range(0, len(new_contact), 4):
        print(f'Контакт "{new_contact[i]} {new_contact[i + 1]} {new_contact[i + 2]} {new_contact[i + 3]}" добавлен в книжку')

# метод добавления контакта
def add_contact(contact):
    # добавляем контакт в конец книжки
    with open("book_people.csv", "a", encoding="utf-8", newline='') as b:

        writer = csv.writer(b, delimiter=',')
        writer.writerow(contact)

    print(f'Контакт "{contact[0]} {contact[1]} {contact[2]} {contact[3]}" добавлен в книжку')

# метод удаления контакта
def del_contact(book, contact):
    
    print(f'Контакт "{book[contact][0]} {book[contact][1]} {book[contact][2]} {book[contact][3]}" удален из книжки')

    # удаляем выбранный контакт
    del book[contact]

    # переписываем книжку без выбранного контакта
    with open("book_people.csv", mode = "w", encoding='utf-8') as b:

        head = ['Имя', 'Фамилия', 'Телефон', 'Описание']

        writer = csv.DictWriter(b, delimiter = ",", lineterminator = "\r", fieldnames = head)
        writer.writeheader()

        for i in range(len(book)):
            writer.writerow({'Имя': book[i][0], 'Фамилия': book[i][1], 'Телефон': book[i][2], 'Описание': book[i][3]})

# метод обновления контакта
def update_contact(book, contact, f):
    # записываем изменения для контакта
    up = input('Введите изменение: ')

    print(f'Контакт "{book[contact][0]} {book[contact][1]} {book[contact][2]} {book[contact][3]}" изменен')

    # переписываем старое значение контакта
    book[contact][f] = up

    # переписываем книжку с изменным контактом
    with open("book_people.csv", mode = "w", encoding='utf-8') as b:

        head = ['Имя', 'Фамилия', 'Телефон', 'Описание']

        writer = csv.DictWriter(b, delimiter = ",", lineterminator = "\r", fieldnames = head)
        writer.writeheader()

        for i in range(len(book)):
            writer.writerow({'Имя': book[i][0], 'Фамилия': book[i][1], 'Телефон': book[i][2], 'Описание': book[i][3]})
