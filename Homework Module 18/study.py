import telebot
from extensions import APIExeption, CashConverter
from config import TOKEN, keys

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome_and_help(message):
    bot.send_message(message.chat.id, f"Приветствую, {message.chat.first_name}! Я помогу тебе посчитать цену на заданное количество валюты. Необходимо отправить сообщение в виде: <имя валюты, цену которой ты хочешь узнать> <имя валюты, в которой хочешь узнать цену первой валюты> <количество первой валюты>")
    bot.send_message(message.chat.id, f"Чтобы ознакомится со списком известных мне валют, введи команду /values")

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=["text"])
def convert(message: telebot.types.Message):
    try:
        value = message.text.split(" ")

        if len(value) > 3:
            raise APIExeption("Слишком много параметров")
        elif len(value) < 3:
            raise APIExeption("Параметров недостаточно")

        quote, base, amount = value
        total_price = CashConverter.get_price(base, quote, amount)
    except APIExeption as e:
        bot.reply_to(message, f'Ошибка ввода\n{e}')
    except Exception as e:
        bot.reply_to(message, f'В данный момент затрудняюсь ответить\n{e}')
    else:
        text = f"За {amount} {quote} придется заплатить {total_price} {base}"
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)