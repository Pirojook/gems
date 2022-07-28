import telebot
# import sqlite3
from telebot import *
from sqlite3 import *
# global db
# global sql

# db = sqlite3.connect('idiot.db', check_same_thread=False)
# sql = db.cursor()

token = "5407078790:AAEgJ7n2eRXZOjMiKyKVvNhuaXjHaTs4ZPs"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    # global user_login
    # user_login = message.from_user.id
    bot.send_message(message.chat.id, "Привествуем в нашем боте, вы можете купить гемов себе на акк")
    
    # sql.execute(f"SELECT login FROM list WHERE login = '{user_login}'")
    # if sql.fetchone() is None:
    #     sql.execute(f"INSERT INTO list VALUES(?, ?)", (user_login, 0))
    #     db.commit()

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)