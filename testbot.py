import telebot

bot = telebot.TeleBot('364248746:AAFiOrNMUZzU0UWkLuFAR94w9tMahv2kdRg')

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('/start')
    user_markup.row('/help')
    bot.send_message(message.from_user.id, "Добро пожаловать!", reply_markup=user_markup)

@bot.message_handler(commands=['help'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('/start')
    user_markup.row('/help')
    answer = """
    Этот Бот умеет разпозновть породу собак и кошек по фотографии.
    Инструкция по использованию:
    1. Если вы хотите определить породу по фотографии с вашего устройства, достаточно отправить ее этому боту и в течение нескольких минут вы получите результат.
    2. Так же есть возможность определить фотогрфию по ссылке. Отправтье боту сообщение в формате 'url + ссылка на фотографию'. сылка должна быть на файл в формате jpg.
    Через несколько минут вы получите ответ.
    """
    bot.send_message(message.from_user.id, answer, reply_markup=user_markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)