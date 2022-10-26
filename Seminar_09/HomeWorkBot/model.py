import csv

# метод чтения всех контактов в базе
def read_contacts():
    contacts = []

    # открываем csv и записываем все контакты
    with open("book_people.csv", encoding='utf-8') as p:
        reader = csv.reader(p, delimiter = ',')
        head = next(reader)

        for row in reader:
            contacts.append(row)

    return contacts

# метод добавления нового контакта
def add_contact(contact):
    contact = contact.split(',')

    if len(contact) != 4:
        return 'Контакт введен неправильно и не добавлен в книгу'

    for i in range(0, 4):
        contact[i] = contact[i].strip()

    # добавляем контакт в конец книжки
    with open("book_people.csv", "a", encoding="utf-8", newline='') as b:

        writer = csv.writer(b, delimiter=',')
        writer.writerow(contact)

    message = f'Контакт "{contact[0]} {contact[1]} {contact[2]} {contact[3]}" добавлен в книжку'

    return message

# метод удаления контакта
def del_contact(contact):

    book = read_contacts()
    message = f'Контакт удален: {book[contact][0]} {book[contact][1]} {book[contact][2]} {book[contact][3]}'
    # удаляем выбранный контакт
    del book[contact]

    # переписываем книжку без выбранного контакта
    with open("book_people.csv", mode = "w", encoding='utf-8') as b:

        head = ['Имя', 'Фамилия', 'Телефон', 'Описание']

        writer = csv.DictWriter(b, delimiter = ",", lineterminator = "\r", fieldnames = head)
        writer.writeheader()

        for i in range(len(book)):
            writer.writerow({'Имя': book[i][0], 'Фамилия': book[i][1], 'Телефон': book[i][2], 'Описание': book[i][3]})
    
    return message

# метод поиска контакта/контактов в книжке
def find_contact(contact):

    book = read_contacts()
    message = 'Такого контакта нет в книжке'
    count = 1

    for i in range(len(book)):
        
        for f in range(0, 4):
            
            if book[i][f] == contact:

                if count >= 2:
                    message += f'{count} - {book[i][0]} {book[i][1]} {book[i][2]} {book[i][3]}\n'
                else:
                    message = f'{count} - {book[i][0]} {book[i][1]} {book[i][2]} {book[i][3]}\n'
            
                count += 1

    return message       

# метод вывода вех контактов
def show_contacts():
    count = 1
    contacts = read_contacts()
    message = ''

    # получившийся список данных выводим в нужном формате
    for i in range(len(contacts)):

        message += f'{count} - {contacts[i][0]} {contacts[i][1]} {contacts[i][2]} {contacts[i][3]}\n'
        count += 1

    return message
