import model

# метод показа меню и определения выбора функции пользователем
def menu():
    print('1 - показать все контакты')
    print('2 - экспортировать контакт')
    print('3 - импортировать контакт')
    print('4 - добавить контакт')
    print('5 - удалить контакт')
    print('6 - изменить контакт')
    print()
    option = input('Выберите функцию ')

    # возвращаем выбор пользователя
    return option

# метод для вывода всех контактов из книжки
def show_contacts(func):
    count = 1
    # обращаемся к model чтобы он считал все наши записанные контакты
    contact = model.read_contacts()

    # получившийся список данных выводим в нужном формате
    for i in range(len(contact)):

        print(f'{count} - {contact[i][0]} {contact[i][1]} {contact[i][2]} {contact[i][3]}')
        count += 1

    # если был выбран экспорт то вернем полученный список
    if func == 2:
        return contact

# метод для показа и получения дополнительной информации после выбора функции
def info(func):
    if func == 2:
        contact = int(input('Введите номер контакта который хотите экспортировать - '))
        file = input('Введите имя файла и его формат в котором хотите получить контакт (пример: file.csv): ')

        # возвращаем номер контакта и имя файла в который занесем выбранный контакт
        return contact - 1, file

    if func == 3:
        file = input('Введите имя файла и его формат из которого хотите импортировать контакты (пример: file_new.csv): ')
        return file

    if func == 4:
        contact = []
        contact.append(input('Введите Имя - '))
        contact.append(input('Введите Фамилию - '))
        contact.append(input('Введите Телефон - '))
        contact.append(input('Введите Описание - '))

        return contact

    if func == 5:
        contact = int(input('Введите номер контакта который хотите удалить - '))

        return contact - 1
    
    if func == 6:

        contact = int(input('Введите номер контакта для изменения - '))

        print('Что вы хотите изменить:')
        print('1 - Имя')
        print('2 - Фамилию')
        print('3 - Телефон')
        print('4 - Описание')

        f = int(input('Введите номер - '))
        
        return contact - 1, f - 1
