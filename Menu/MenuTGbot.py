import os
import sys
import telebot
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from Menu.orm_menu import (MenuORM_createTable, MenuORM_return,
                           CreateTable_temporary, MenuORM_TableUsers)
from Menu.menu_data import menu_parents

#Наше меню, которое в дальнейшем будет собиратся из приложений



def CreateMenu (isCreate=True):
    menu_orm = MenuORM_createTable ()
    if isCreate:
        menu_orm.create_tables()
        menu_orm.insert_menu_parent(menu_parents)
        menu_orm.insert_menu_daughter(menu_parents)



class MenuTGbot:
    def CreateTable_MenuTGbot(self):
        MenuORM_createTable.create_tables()
        MenuORM_createTable.insert_menu_parent(menu_parents)
        MenuORM_createTable.insert_menu_daughter(menu_parents)


class Menu_bot:

    def create_menu(self, txt_in):
        """
        Создаем меню
        :param txt_in:

        :return:
        возвращаем main_menu объект для работы bot

        """
        menu_titles = self.menu_titles(txt_in)
        print(f' menu_titles = {menu_titles}', type (menu_titles))
        main_menu = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        for menu_title in menu_titles:
            print(f'menu_title = {menu_title}')
            main_menu.add(menu_title)
        return main_menu
    @staticmethod
    def menu_titles(txt_in):
        if txt_in == '/menu':
            parent_in = 'G'
            tittlenamemenu = MenuORM_return.select_table_MenuParents(parent_in)
        else:
            parent_in = txt_in
            tittlenamemenu = MenuORM_return.select_table_MenuDaughter(parent_in)
        return tittlenamemenu
    @staticmethod
    def menu_define_iswork (tittlenamemenu):

        if tittlenamemenu != '/menu':
            iswork = MenuORM_return.select_table_MenuDaughter_iswork(tittlenamemenu)
            if iswork:
                description = MenuORM_return.select_table_MenuDaughter_description(tittlenamemenu)
                text_for_msg = description
                pass
            else:
                print('Не работает')
                t = "\U0001F528"
                list_all_work_section = MenuORM_return.select_table_MenuDaughter_iswork_True()
                text_for_msg = '\n'.join([f"{i+1}.\t{item}" for i, item in enumerate(list_all_work_section)])
                a = f"Выбранный раздел: <b>{tittlenamemenu} </b> находится на этапе разработки " + t + '\n'
                b = '\n' + "Можете выбрать один из следующих разделов:\n" + text_for_msg + '\n'
                c = '\n\t' + "Что бы обновить меню вызовите /menu"
                text_for_msg = a + b + c

        else:
            text_for_msg = ''
            # выбери другой раздел
            # запроос на те селекты, которые iswork рабочий

        return text_for_msg

    @staticmethod
    def return_all_list_menu():
        tittlenamemenu = MenuORM_return.return_tittlenamemenus()
        return tittlenamemenu

    @staticmethod
    def save_select_title_user (user_data):
        isUser = MenuORM_TableUsers.select_table_MenuUser(user_data)
        print(f'isUser = {isUser}')
        if isUser == []:
            MenuORM_TableUsers.insert_table_users(user_data)
            pass
        else:
            MenuORM_TableUsers.update_table_users(user_data)
            MenuORM_TableUsers.test_test(user_data)
            pass


        # значит вовзращаем пользователю меню
        pass



def Create_temporary_table(Name_Table):
    test = CreateTable_temporary()
    test.create_new(Name_Table)

#"Создади декоратор для фильтрации"
def check_message_in_filter(list_filter):
    def decorator(func):
        def wrapper(message):
            if message.text in list_filter:
                return func(message)
            else:

                pass
        return wrapper
    return decorator