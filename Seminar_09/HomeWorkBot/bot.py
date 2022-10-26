from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
import model

# ТОКЕН бота
bot_token = 'ТОКЕН'
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher



# метод начала
def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Я создан для работы с телефонной книгой\n/help - показать доступные команды")

# метод для вывода всех команд
def help(update, context):
    update.message.reply_text(f'/showall - показать все контакты\n/find - найти контакт по фамилии\n/addcontact - добавить контакт\n/deletecontact - удалить контакт')

# метод вывода всех контактов
def showall(update, context):
    update.message.reply_text(model.show_contacts())

# метод вывода искомого контакта
def find(update, context):
    update.message.reply_text(model.find_contact(update.message.text))

# метод вывода удаленного контакта
def delete(update, context):
    update.message.reply_text(model.del_contact(int(update.message.text) - 1))

# метод получения ключевого слова
def choose_contact(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите имя, фамилию, номер или описание')
    context.bot.send_message(update.effective_chat.id, '/stop чтобы выйти из режима поиска')
    return 1

# метод получения номера нужного контакта
def choose_to_del(update, context):
    update.message.reply_text(model.show_contacts())
    context.bot.send_message(update.effective_chat.id, 'Введите номер контакта который хотите удалить')
    context.bot.send_message(update.effective_chat.id, '/stop чтобы выйти из режима удаления контактов')
    return 2

# метод остановки
def stop(update, context):
    update.message.reply_text('Вы вышли из режима')
    return bot.ConversationHandler.END

# метод получения нового контакта
def add(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите Имя, Фамилию, Номер, Описание через запятую')
    return 3

# метод вывода контакта который получили
def create_contact(update, context):
    update.message.reply_text(model.add_contact(update.message.text))
    context.bot.send_message(update.effective_chat.id, '/stop чтобы выйти из режима добавления контактов')



# хендлеры для команд
find_handler = ConversationHandler(

        entry_points=[CommandHandler('find', choose_contact)],

        states={
            1: [MessageHandler(Filters.text & ~Filters.command, find)]
        },

        fallbacks=[CommandHandler('stop', stop)]
    )

start_handler = CommandHandler('start', start)

help_handler = CommandHandler('help', help)

showall_handler = CommandHandler('showall', showall)

delete_handler = ConversationHandler(

        entry_points=[CommandHandler('deletecontact', choose_to_del)],

        states={
            2: [MessageHandler(Filters.text & ~Filters.command, delete)]
        },

        fallbacks=[CommandHandler('stop', stop)]
    )

add_handler = ConversationHandler(

        entry_points=[CommandHandler('addcontact', add)],

        states={
            3: [MessageHandler(Filters.text & ~Filters.command, create_contact)]
        },

        fallbacks=[CommandHandler('stop', stop)]
    )



# диспатчеры команд
dispatcher.add_handler(find_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(showall_handler)
dispatcher.add_handler(delete_handler)
dispatcher.add_handler(add_handler)



updater.start_polling()

print("Бот включен")

updater.idle()
