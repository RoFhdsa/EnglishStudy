import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from Menu.orm_menu import MenuORM_createTable

#Наше меню, которое в дальнейшем будет собиратся из приложений
menu_parents = [{"tittlenamemenu": "Прочие запросы", "labale": "B", "parent": "G"},
                {"tittlenamemenu": "🏆 Выбор тренировки", "labale": "A", "parent": "G"},
                {"tittlenamemenu": "🌍 Перевод", "labale": "A1", "parent": "A"},
                {"tittlenamemenu": "🇬🇧🔄🇷🇺 Перевод с Английского на Русский", "labale": "A1A", "parent": "A1"},
                {"tittlenamemenu": "🇷🇺🔄🇬🇧 Перевод русского на Английский", "labale": "A1B", "parent": "A1"},
                {"tittlenamemenu": "Неправильные глаголы", "labale": "A2", "parent": "A"},
                {"tittlenamemenu": "🖼️🇷🇺🔄🇬🇧 Перевод картинки", "labale": "A3", "parent": "A"},
                {"tittlenamemenu": "🇷🇺🔄🇬🇧📝 Глагол в инфинитиве", "labale": "A2A", "parent": "A2"},
                {"tittlenamemenu": "🇷🇺🔄🇬🇧4️⃣📝 Глагол 4 формы", "labale": "A2B", "parent": "A2"},
                {"tittlenamemenu": "🌐📷✍️🇬🇧 Картинка из интернета", "labale": "A3A", "parent": "A3"}]


def CreateMenu (isCreate=True):
    menu_orm = MenuORM_createTable ()
    if isCreate:menu_orm.create_tables()
    menu_orm.insert_menu_parent(menu_parents)
    menu_orm.insert_menu_daughter(menu_parents)

class MenuTGbot:
    def __init__(self):
        self.create_menuParents = MenuORM.create_tables()
        self.insert_menuParents = MenuORM.insert_menu_parent(menu_parents)
        self.insert_daughter = MenuORM.insert_menu_daughter(menu_parents)
