import telebot
import config
import PIL.Image
from telebot import types
import neural as nn

bot = telebot.TeleBot(config.token)


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


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('/start')
    user_markup.row('/help')

    file_id = message.photo[2].file_id
    path = bot.get_file(file_id)
    url = 'https://api.telegram.org/file/bot' + str(config.token) + '/' + str(path.file_path)
    nn.download(url,
                'test')
    list_file = nn.begin('test')

    # img = message.photo[0]
    # PIL.Image.fromarray(img).save('test.jpg', 'jpeg')
    animal = list_file[0].split(' ')
    answer = 'На картинке ' + animal[0] + ' с вероятностью ' + animal[1] + ' процентов.'
    bot.send_message(message.from_user.id, answer, reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('/start')
    user_markup.row('/help')
    message_list = message.text.split(' ')
    print(message_list)
    if message_list[0] == 'url' and len(message_list)>1:
        url = message_list[1]
        try:
            nn.download(url, 'test')
        except ValueError:
            print('error')
            bot.send_message(message.from_user.id, 'Неправильно указан url', reply_markup=user_markup)
            return
        list_file = nn.begin('test')
        animal = list_file[0].split(' ')
        answer = 'На картинке ' + animal[0] + ' с вероятностью ' + animal[1] + ' процентов.'
        bot.send_message(message.from_user.id, answer, reply_markup=user_markup)

    else:
        bot.send_message(message.chat.id, 'Неправильно указан url', reply_markup=user_markup)


if __name__ == '__main__':
    bot.polling(none_stop=True)
