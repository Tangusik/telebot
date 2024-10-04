from all_tokens import TOKEN
import telebot
from telebot import types
from db import DBWorker

db=DBWorker()
bot = telebot.TeleBot(TOKEN)


letters= ["А","Б","В","Г","Д","Е","Ё","Ж","З","К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Э","Ю","Я"]
letter_btns=[types.InlineKeyboardButton(text=letter, callback_data=letter) for letter in letters]

letter_markup = types.InlineKeyboardMarkup()
letter_markup.row(letter_btns[0], letter_btns[1], letter_btns[2],  letter_btns[3], letter_btns[4])
letter_markup.row(letter_btns[5], letter_btns[6], letter_btns[7],  letter_btns[8], letter_btns[9])
letter_markup.row(letter_btns[10], letter_btns[11], letter_btns[12],  letter_btns[13], letter_btns[14])
letter_markup.row(letter_btns[15], letter_btns[16], letter_btns[17],  letter_btns[18], letter_btns[19])
letter_markup.row(letter_btns[20], letter_btns[21], letter_btns[22],  letter_btns[23], letter_btns[24])
letter_markup.row(letter_btns[25], letter_btns[26], letter_btns[27])



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Хочу найти работу")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой <s>ЦАРЬ И БОГ</s> бот-помошник в поиске работы). ", reply_markup=markup, parse_mode="HTML")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Хочу найти работу':
        markup = letter_markup

        bot.send_message(message.from_user.id, 'Выберите первую букву своего города', reply_markup=markup) 


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data in letters:
        db.cursor.execute(f"SELECT title FROM lc_city WHERE title ^@ '{callback.data}'")
        cities = db.cursor.fetchall()
        cities = [c[0] for i,c in enumerate(cities)]
        
        city_markup = types.InlineKeyboardMarkup()
        if cities:
            for city in cities:
                city_markup.row(types.InlineKeyboardButton(text=city, callback_data=city))
            bot.send_message(callback.message.chat.id, f"Ты ищешь город на букву {callback.data}", reply_markup=city_markup)
        else:
            bot.send_message(callback.message.chat.id, f"Ты ищешь город на букву {callback.data}. К сожалению пока нет вакансий в этих городах")
        

bot.polling(none_stop=True, interval=0)
