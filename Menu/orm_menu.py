from sqlalchemy import text, insert, select
from database import syns_engine, sessionMy, Base, DeclarativeBase
from Menu.models_menu import MenuParents, MenuDaughter, MenuUser, create_table_class

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
                row = MenuParents (
                    tittlenamemenu = menu_parents_rows ['tittlenamemenu'],
                    labale=menu_parents_rows['labale'],
                    parent=menu_parents_rows['parent'],
                    description=menu_parents_rows['description'],
                    iswork = menu_parents_rows['iswork'])
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
                isLabale = self.select_table_MenuParents_labale(menu_parents_rows['labale'])

                row = MenuDaughter(
                                tittlenamemenu=menu_parents_rows['tittlenamemenu'],
                                labale=menu_parents_rows['labale'],
                                daughter= isLabale[0],
                                daughter_tittlenamemenu=isLabale[1],
                                description=menu_parents_rows['description'],
                                iswork = menu_parents_rows['iswork']
                )
                session.add(row)
            session.commit()

    @staticmethod
    def select_table_MenuParents_labale(Daughter_Lable):
        """
        :param Daughter_Lable:
        :return:
        """
        with sessionMy() as session:
            print(f'WHERE = {Daughter_Lable}')
            sub_query = (
                select(
                    MenuParents.labale.distinct().label("labale")
                ).select_from(MenuParents)
                .filter(MenuParents.parent == Daughter_Lable)
            )
            res_1 = session.execute(sub_query)
            labale_l = res_1.all()
            result_sub_query = ','.join(i[0] for i in labale_l)

            query = select (
                MenuParents.tittlenamemenu
            ).filter(MenuParents.labale == sub_query.c.labale)
            res_1 = session.execute(query)
            labale_l = res_1.all()
            query = ','.join(i[0] for i in labale_l)

            #Не используется:
            query_isWork = select (
                MenuParents.iswork
            ).filter(MenuParents.labale == sub_query.c.labale)
            res_1 = session.execute(query_isWork)
            labale_l = res_1.all()
            labale_l = [X[0] for X in labale_l]
            print(f'labale_l = {labale_l}')
            if True in labale_l:
                isWork = True
            else:
                isWork = False


        return result_sub_query, query, isWork



    #Обновить данные в б БД по ключу
    #Передаем в функцию параметр ключа и новое значение
    @staticmethod
    def update_table_menu (id: int = 1, new_username: str = "kot"):
        with sessionMy() as session:
            pass

class MenuORM_return:

    @staticmethod
    def select_table_MenuParents(parent_in):
        print(f' parent_in - select_table_MenuParents = {parent_in}', type(parent_in))
        with sessionMy() as session:
            query = (select(MenuParents.tittlenamemenu).select_from(MenuParents)
                        .filter(MenuParents.parent == parent_in))
            res_1 = session.execute(query)
            tittlenamemenu = res_1.all()
            tittlenamemenu = [X[0] for X in tittlenamemenu]
            print(f' select_table_MenuParents = {tittlenamemenu}', type(tittlenamemenu))
        return tittlenamemenu

    @staticmethod
    def select_table_MenuDaughter(tittlenamemenu_user):
        print(f' parent_in - select_table_MenuParents = {tittlenamemenu_user}', type(tittlenamemenu_user))
        with sessionMy() as session:
            query_daughter_tittlenamemenu = (select(MenuDaughter.daughter_tittlenamemenu)
                        .filter(MenuDaughter.tittlenamemenu == tittlenamemenu_user))
            res_1 = session.execute(query_daughter_tittlenamemenu)
            daughter_tittlenamemenu = res_1.all()
            daughter_tittlenamemenu = [X[0] for X in daughter_tittlenamemenu] [0].split(',')
            print(f' select_table_MenuParents = {daughter_tittlenamemenu}', type(daughter_tittlenamemenu))
        return daughter_tittlenamemenu

    @staticmethod
    def select_table_MenuDaughter_description (tittlenamemenu_user):
        print( f' select_table_MenuDaughter_description tittlenamemenu_user = {tittlenamemenu_user}')
        with sessionMy() as session:
            query_daughter_description = (select(MenuDaughter.description)
                        .filter(MenuDaughter.tittlenamemenu == tittlenamemenu_user))
            res_1 = session.execute(query_daughter_description)
            output = res_1.first()
            print(f' select_table_MenuDaughter_description  = {output}', type(output))
        return output

    @staticmethod
    def select_table_MenuDaughter_iswork(tittlenamemenu_user):
        print(f' select_table_MenuDaughter_iswork tittlenamemenu_user = {tittlenamemenu_user}', type(tittlenamemenu_user))
        with sessionMy() as session:
            query_daughter_isWork = (select(MenuDaughter.iswork)
                        .filter(MenuDaughter.tittlenamemenu == tittlenamemenu_user))
            res_1 = session.execute(query_daughter_isWork)
            output = res_1.first()
            print(f' select_table_MenuDaughter_iswork = {output [0]}', type(output[0]))
        return output [0]
    @staticmethod
    def select_table_MenuDaughter_iswork_True():

        with sessionMy() as session:
            query_daughter_tittlenamemenu = (select(MenuDaughter.tittlenamemenu)
                        .filter(MenuDaughter.iswork == True))
            res_1 = session.execute(query_daughter_tittlenamemenu)
            output = res_1.all()
            print(f' select_table_MenuDaughter_iswork = {output}', type(output))
            output = [X[0] for X in output]
            print(f' select_table_MenuDaughter_iswork = {output}', type(output))
        return output

    @staticmethod
    def return_tittlenamemenus():
        "Переиспользуем для фильтра и валидации меню"
        with sessionMy() as session:
            query = (
                select(
                    MenuParents.tittlenamemenu
                ).select_from(MenuParents)
            )
            res_1 = session.execute(query)
            tittlenamemenu = res_1.all()
            tittlenamemenu = [X[0] for X in tittlenamemenu]
            print(f' return_tittlenamemenus _ after  = {tittlenamemenu}', type(tittlenamemenu))
        return tittlenamemenu



class MenuORM_TableUsers:
    @staticmethod
    def insert_table_users(user_data):
        row =  MenuUser (user_id = user_data['user_id'] ,user_name= user_data['user_name'] ,
                         user_name_id= user_data['user_name_id'] , tittlenamemenu_choised = user_data['tittlenamemenu_choised'] )
        with sessionMy() as session:
            session.add (row)
            session.commit()
        pass

    @staticmethod
    def update_table_users (user_data):
        user_name_id_in = user_data ['user_name_id']
        x = user_data['tittlenamemenu_choised']
        print(f'user_data [tittlenamemenu_choised] = {x}')
        new_tittlenamemenu_choised = user_data ['tittlenamemenu_choised']
        with sessionMy() as session:
            print(f'user_name_id_in = {user_name_id_in}')
            row_MenuUser = session.query(MenuUser).filter_by(user_name_id=user_name_id_in).first()
            if row_MenuUser:
                row_MenuUser.tittlenamemenu_choised = new_tittlenamemenu_choised
                session.commit()
                print("Данные успешно обновлены")
            query = (select(MenuUser.tittlenamemenu_choised).filter(MenuUser.user_name_id == user_name_id_in))
            res_1 = session.execute(query)
            tittle = res_1.all()
            print(f' tittle = {tittle}')
            pass

    @staticmethod
    def test_test (user_data):
        user_name_id_in = user_data ['user_name_id']
        with sessionMy() as session:
            query = (select(MenuUser.tittlenamemenu_choised).filter(MenuUser.user_name_id == user_name_id_in))
            res_1 = session.execute(query)
            tittle = res_1.all()
            print(f' tittle = {tittle}')
            pass


    @staticmethod
    def select_table_MenuUser (user_data):
        """
        Проверяем если в таблице menu_user пользователь
        :param user_data:
        :return:
        """
        user_name_id = user_data ['user_name_id']
        print(f'user_name_id = {user_name_id}')
        with sessionMy() as session:
            query = (select(MenuUser.user_name_id).filter(MenuUser.user_name_id == user_name_id))
            res_1 = session.execute(query)
            user_name_id = res_1.all()

            # возможно ли так сократить запрос row_MenuUser = session.get(MenuUser, user_name_id)
            print (f'user_name_id -- = {user_name_id}')
        return user_name_id

class CreateTable_temporary():
    @staticmethod
    def create_new(table_name):
        DynamicTable = create_table_class(table_name)
        DynamicTable.__table__.create(bind=syns_engine)