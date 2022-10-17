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

    # Если была введена не правильная цифра"
    else:
        print('Функция не выбрана')