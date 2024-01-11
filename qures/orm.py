from sqlalchemy import text, insert, select
from database import syns_engine, sessionMy, Base, DeclarativeBase
from models import Worker, ResumeOrm
from Menu.models_menu import Menu

#ResumeOrm = ResumeOrm()

class SyncORM:
    @staticmethod
    def create_tables ():
        Base.metadata.drop_all(syns_engine)
        syns_engine.echo = True
        Base.metadata.create_all(syns_engine)

    @staticmethod
    def insert_tables():
        Worker_bobr = Worker (username = 'bobr')
        Worker_volk = Worker (username = 'volk')
        Worker_zebra = Worker (username = 'zebra')
        with sessionMy() as session:
            session.add_all ([Worker_bobr, Worker_volk,Worker_zebra])
            session.commit()
    @staticmethod
    def insert_tables_ResumeOrm():
        Worker_bobr = ResumeOrm (title = 'QA Ingener', compensation = 1000, workload = 'parttime', worker_id = 1)
        with sessionMy() as session:
            session.add_all ([Worker_bobr])
            session.commit()
    @staticmethod
    def select_tables():
        with sessionMy() as session:
            id = 1
            query = session.get(Worker, id)
            print(f'{query = }')
            query = select (Worker)
            result = session.execute(query)
            workers = result.scalars().all()
            print(f'{workers = }')

    #Обновить данные в б БД по ключу
    #Передаем в функцию параметр ключа и новое значение
    @staticmethod
    def update_tables(id: int = 1, new_username: str = "kot"):
        with sessionMy() as session:
            query = session.get(Worker, id)
            query.username = new_username
            session.commit()
