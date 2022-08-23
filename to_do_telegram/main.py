import func as f
import os
import telebot
token = '5704577691:AAH_QilgsdpqJJGgUE5BcVc9TAXFdHmVOTM'
from telebot import types

bot = telebot.TeleBot(token)

markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton('Посмотреть список дел')
button2 = types.KeyboardButton('Создать новую задачу')
button3 = types.KeyboardButton('Очистить список дел')
button4 = types.KeyboardButton('Выйти')
markup.add(button1, button2, button3, button4)


@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет, я твой список дел ✌️ Выбери, что хочешь сделать: ", reply_markup=markup)

@bot.message_handler()
def handle_message(msg):
    chat_id = str(msg.chat.id)

    if msg.text == button1.text:
        json_data = f.read_from_file()
        to_do_list = json_data.get(str(chat_id), [])
        if len(to_do_list) == 0:
            bot.send_message(chat_id, 'В списке дел нет задач', reply_markup=markup)
            return

        to_do_body = 'Текущие дела: \n'
        for i, j in enumerate(to_do_list):
            to_do_body += f'\n{i}) {j}\n'
        bot.send_message(chat_id, to_do_body)

        list_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        edit_button = types.KeyboardButton('Редактировать')
        delete_button = types.KeyboardButton('Удалить')
        cancel_button = types.KeyboardButton('Назад')
        list_markup.add(edit_button, delete_button, cancel_button)
        bot.send_message(chat_id, 'Выберите действие', reply_markup=list_markup)

    if msg.text == 'Редактировать':
        bot.send_message(chat_id, 'Введите номер задачи, которую надо отредактировать: ')
        bot.register_next_step_handler(msg, edit_task)

    if msg.text == 'Удалить':
        bot.send_message(chat_id, 'Введите номер задачи, которую надо удалить: ')
        bot.register_next_step_handler(msg, delete_task)

    if msg.text == 'Назад':
        bot.send_message(chat_id, 'Возврат в главное меню', reply_markup=markup)
        
    if msg.text == button2.text:
        json_data = f.read_from_file()
        bot.send_message(chat_id, 'Напиши, какую задачу добавить')
        bot.register_next_step_handler(msg, add_task_into_list)

    if msg.text == button3.text:
        json_data = f.read_from_file()
        json_data[chat_id] = []
        f.write_to_file(json_data)
        bot.send_message(chat_id, 'Все задачи удалены', reply_markup=markup)

def add_task_into_list(message):
    chat_id = str(message.chat.id)
    json_data = f.read_from_file()
    list_to_do = json_data.get(chat_id, [])
    list_to_do.append(message.text)
    json_data[chat_id] = list_to_do
    f.write_to_file(json_data)
    bot.send_message(chat_id, 'Задача добавлена', reply_markup=markup)  

def edit_task(message):
    chat_id = str(message.chat.id)
    json_data = f.read_from_file()
    list_to_do = json_data.get(chat_id, [])
    try:
        to_do_index = int(message.text)
    except ValueError:
        bot.send_message(chat_id, 'Надо ввести номер задачи')
        return

    if to_do_index < 0 or to_do_index > len(list_to_do):
        bot.send_message(chat_id, 'Надо ввести существующий номер задачи')
        return 

    def edit_main(msg):
        list_to_do[to_do_index] = msg.text
        json_data[chat_id] = list_to_do
        f.write_to_file(json_data)
        bot.send_message(chat_id, 'Изменения сохранены', reply_markup=markup)
    bot.send_message(chat_id, 'Что будет в этой задаче?')
    bot.register_next_step_handler(message, edit_main)

def delete_task(message):
    chat_id = str(message.chat.id)
    json_data = f.read_from_file()
    list_to_do = json_data.get(chat_id, [])
    try:
        to_do_index = int(message.text)
    except ValueError:
        bot.send_message(chat_id, 'Надо ввести номер задачи')
        return

    if to_do_index < 0 or to_do_index > len(list_to_do):
        bot.send_message(chat_id, 'Надо ввести существующий номер задачи')
        return

    del list_to_do[to_do_index]
    json_data[chat_id] = list_to_do
    f.write_to_file(json_data)
    bot.send_message(chat_id, 'Задача удалена')


print('server started')
bot.infinity_polling()