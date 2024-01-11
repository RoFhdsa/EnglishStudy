from sqlalchemy import text, insert
from database import syns_engine
from models import metadata_obj, worker_table

def create_tables ():
    metadata_obj.drop_all(syns_engine)
    metadata_obj.create_all(syns_engine)

def insert_tables():
    with syns_engine.connect() as conn:
        stm = insert (worker_table).values(
            [
                {"username": 'Bobr'},
                {"username":'Volk'}
            ]
        )
        conn.execute(stm)
        conn.commit()