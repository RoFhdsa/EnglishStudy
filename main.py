import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
import telebot

#from qures.orm import SyncORM
#from Menu.orm_menu import MenuORM
#MenuORM.create_tables()
#MenuORM.insert_menu()
from Menu.MenuTGbot import MenuTGbot, CreateMenu, Menu_bot, Create_temporary_table, check_message_in_filter
from ACCESSORY.my_lib_def import retern_dict_use_data

#MenuTGbot = MenuTGbot()
CreateMenu(isCreate=True)

bot = telebot.TeleBot('6225588552:AAHCipXm3p4sY4jcrprdEkjNivaDNFikYfc')

@bot.message_handler(commands=['menu'])
def start_message(message):
    menu_bot = Menu_bot()
    Keyboard = menu_bot.create_menu(message.text)
    print(f'message.text = {message.text}')
    bot.send_message(message.chat.id, text='чтобы обновить /menu', reply_markup=Keyboard)
    user_data = retern_dict_use_data (message)
    menu_bot.save_select_title_user(user_data)


@bot.message_handler(content_types=['text'], func=lambda message: True)
@check_message_in_filter(Menu_bot.return_all_list_menu())
def send_text(message):
    menu_bot = Menu_bot()
    Keyboard = menu_bot.create_menu(message.text)
    user_data = retern_dict_use_data(message)
    menu_bot.save_select_title_user(user_data)
    t = "\U0001F528"
    d = """<pre>pre-formatted fixed-width code block</pre>"""
    d = """<tg-emoji emoji-id="5368324170671202286">👍</tg-emoji>"""
    a = menu_bot.menu_define_iswork(message.text)
    #a = f'{t}'
    bot.send_message(message.chat.id,
                     parse_mode="HTML",
                     text=a,
                     reply_markup=Keyboard)
    menu_bot.save_select_title_user(user_data)

    pass

@bot.message_handler(content_types=['text'], func=lambda message: True,)
def send_text(message):
    print('обработчик текст')
    NameTable = str(message.from_user.first_name) + str(message.from_user.id)
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    # Как создать табллицу - Create_temporary_table (NameTable)
    pass


bot.polling(none_stop=True, interval=0)
bot.polling()