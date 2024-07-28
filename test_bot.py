import telebot
from telebot import types

TOKEN = '***'
bot = telebot.TeleBot(TOKEN)
CHAT_ID = '***'
USER_ID = '***'

text1 = 'текст1'
text2 = 'текст2'

@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    bot.reply_to(message, "Привет! Запрос?")    
    
@bot.message_handler(func=lambda m: m.text not in ["Жду", "Нет"])
def handle_message(message: telebot.types.Message):
    request = message.text

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Жду"), types.KeyboardButton("Нет"))
    bot.send_message(message.chat.id, "Ждёт?", reply_markup=markup)


@bot.message_handler(func=lambda m: m.text in ["Жду", "Нет"]) 
def handle_response(response: telebot.types.Message):
    if response.text == 'Жду':
        bot.reply_to(response, text1)

        try:
            bot.send_message(CHAT_ID, text1)
        except:
            bot.send_message(response.chat.id, "Такого чата нет")
    elif response.text == 'Нет':
        bot.reply_to(response, text2)

        try:
            bot.send_message(USER_ID, text2)
        except:
            bot.send_message(response.chat.id, "Такого человека нет")

    markup = types.ReplyKeyboardRemove()
    bot.send_message(response.chat.id, "Введите новый запрос", reply_markup=markup)
    

bot.polling()
