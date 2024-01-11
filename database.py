from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine, String
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from sqlalchemy.sql.annotation import Annotated

from config import settings

syns_engine = create_engine (
    url= settings.DATABASE_URL(),
    echo= True
)

sessionMy = sessionmaker(syns_engine)
str_200 = Annotated [str, 200]
class Base (DeclarativeBase):
    type_annotation_map = {
        str_200: String (200)
    }

#with sessionMy() as sessionMy:
