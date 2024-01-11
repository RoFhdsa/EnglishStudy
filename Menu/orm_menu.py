from sqlalchemy import text, insert, select
from database import syns_engine, sessionMy, Base, DeclarativeBase
from Menu.models_menu import MenuParents, MenuDaughter

#ResumeOrm = ResumeOrm()


class MenuORM_createTable:
    @staticmethod
    def create_tables ():
        Base.metadata.drop_all(syns_engine)
        syns_engine.echo = True
        Base.metadata.create_all(syns_engine)

    @staticmethod
    def insert_menu_parent(menu_parents):
        with sessionMy() as session:
            for menu_parents_rows in menu_parents:
                row = MenuParents (tittlenamemenu = menu_parents_rows ['tittlenamemenu'],labale=menu_parents_rows['labale'],parent=menu_parents_rows['parent'] )
                session.add (row)
            session.commit()

    def select_table_MenuParents(Daughter_Lable):
        with sessionMy() as session:
            query = (
                select(
                    MenuParents.parent
                ).select_from(MenuParents)
                .filter(MenuParents.parent == Daughter_Lable)
            )
            res = session.execute(query)
            resulte = res.all()
            print(resulte)
            pass


    def insert_menu_daughter(self, menu_parents):
        with sessionMy() as session:
            for menu_parents_rows in menu_parents:
                row = MenuDaughter(tittlenamemenu=menu_parents_rows['tittlenamemenu'],
                                  labale=menu_parents_rows['labale'], daughter= self.select_table_MenuParents(menu_parents_rows['labale'] ))
                session.add(row)
            session.commit()

    @staticmethod
    def select_table_MenuParents(Daughter_Lable):
        with sessionMy() as session:
            print(f'WHERE = {Daughter_Lable}')
            query = (
                select(
                    MenuParents.labale.distinct()
                ).select_from(MenuParents)
                .filter(MenuParents.parent == Daughter_Lable)
            )
            res_1 = session.execute(query)
            labale_l = res_1.all()
            print(f' labale_l = {labale_l}', type(labale_l))
            result = ','.join(i[0] for i in labale_l)
            print(f' result = {result}', type (result))
            print(4*'------')
        return result



    #Обновить данные в б БД по ключу
    #Передаем в функцию параметр ключа и новое значение
    @staticmethod
    def update_table_menu (id: int = 1, new_username: str = "kot"):
        with sessionMy() as session:
            pass

