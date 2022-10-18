import view
import model

# начало
def run():
    # обращаемся к view для показа меню
    option = view.menu()

    # Начало функции "показать все контакты"
    if option == '1':
        view.show_contacts(1)

    # Начало функции "экспортировать контакт"
    elif option == '2':

        # покажем контакты для выбора
        book = view.show_contacts(2)

        # обращаем к методу для получения и вывода нужной информации
        contact, file = view.info(2)

        # обращаемся к методу для экспорта
        model.export_contact(book, contact, file)

    # Начало функции "импортировать контакт"
    elif option == '3':

        # обращаем к методу для получения и вывода нужной информации
        file = view.info(3)

        # обращаемся к методу для импорта
        model.import_contact(file)
    
    # Начало функции "добавить контакт"
    elif option == '4':
        
        contact = view.info(4)

        model.add_contact(contact)

    # Начало функции "удалить контакт"
    elif option == '5':
        
        book = view.show_contacts(2)

        contact = view.info(5)

        model.del_contact(book, contact)

    # Начало функции "изменить контакт"
    elif option == '6':

        book = view.show_contacts(2)

        contact, f = view.info(6)

        model.update_contact(book, contact, f)

    # Если была введена не правильная цифра"
    else:
        print('Функция не выбрана')
