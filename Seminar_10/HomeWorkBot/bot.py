import model

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters


reply_keyboard = [['/play', '/info', '/close']]
stop_keyboard = [['/stop']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard = False)
stop_markup = ReplyKeyboardMarkup(stop_keyboard, one_time_keyboard = False)

TOKEN = ''


def start(update, context):
    update.message.reply_text("Я бот для игры в конфеты", reply_markup = markup)

def play(update, context):
    update.message.reply_text("Введите количество конфет", reply_markup = stop_markup)
    return 1

# метод для запоминания общего числа конфет
def candies(update, context):
    # записываем общее число конфет
    candy = update.message.text
    
    # если было введено чтото не то, то выдаст ошибку чтобы игрок ввел другое число
    try:
        candy = int(candy)

    except ValueError:
        update.message.reply_text('Введите другое число')
        return 1

    update.message.reply_text('Сколько конфет вы возьмете?')

    # метод для записи числа
    model.game(candy)

    return 2

# метод для игры с ботом
def turn(update, context):
    playertake = update.message.text
    
    # проверка на правильность введеного числа
    try:
        playertake = int(playertake)

        if playertake > 28 or playertake < 1:
            update.message.reply_text('Введите другое число')
            return 2

    except ValueError:
        update.message.reply_text('Введите другое число')
        return 2

    model.player(playertake)

    update.message.reply_text(f'Вы взяли {playertake} конфет\nКонфет осталось {model.candy}')
    
    # проверяем закончилась ли игра
    if model.candy <= 28:
        
        update.message.reply_text(f'Победил бот!')
        return ConversationHandler.END

    bottake = model.bot()

    update.message.reply_text(f'Бот взял {bottake} конфет\nКонфет осталось {model.candy}')
    
    # проверяем закончилась ли игра
    if model.candy <= 28:
        
        update.message.reply_text(f'Вы победили!')
        return ConversationHandler.END
    
    update.message.reply_text('Сколько конфет вы возьмете?')

    return 2

def stop(update, context):
    update.message.reply_text("Пока", reply_markup = markup)
    
    return ConversationHandler.END

def info(update, context):
    update.message.reply_text("На столе лежит 2021 конфета.\nИгроки делают ход после друг друга.\nПервый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход.")

def close(update, context):
    update.message.reply_text("Игра закончена", reply_markup = ReplyKeyboardRemove())


play_handler = ConversationHandler(
    entry_points = [CommandHandler('play', play)],

    states = {
        1: [MessageHandler(Filters.text & ~Filters.command, candies)],
        2: [MessageHandler(Filters.text & ~Filters.command, turn)]
    },

    fallbacks = [CommandHandler('stop', stop)]
)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(play_handler)
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("close", close))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
