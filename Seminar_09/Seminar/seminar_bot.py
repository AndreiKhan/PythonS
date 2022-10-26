from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from random import randint

bot_token = 'ТОКЕН'
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет! Это калькулятор\nВыберите рассчет (кг в гр) /convert\nРассчитать значение выражения /calc")


def convert(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите количество килограмм')
    return 1


def convert_output(update, context):
    update.message.reply_text(f'{int(update.message.text) * 1000} грамм')


def calc(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите выражение')
    return 1


def calc_output(update, context):
    update.message.reply_text(eval(update.message.text))


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


convert_handler = ConversationHandler(

        entry_points=[CommandHandler('convert', convert)],

        states={
            1: [MessageHandler(Filters.text & ~Filters.command, convert_output)]
        },

        fallbacks=[CommandHandler('stop', stop)]
    )

calc_handler = ConversationHandler(

        entry_points=[CommandHandler('calc', calc)],

        states={
            1: [MessageHandler(Filters.text & ~Filters.command, calc_output)]
        },

        fallbacks=[CommandHandler('stop', stop)]
    )

start_handler = CommandHandler('start', start)

dispatcher.add_handler(convert_handler)
dispatcher.add_handler(calc_handler)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()
