from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class MenuParents(Base):
    __tablename__ = 'menu_parents'
    id: Mapped  [int] = mapped_column(primary_key=True)
    tittlenamemenu: Mapped [str]
    labale: Mapped [str]
    parent: Mapped [str]

class MenuDaughter(Base):
    __tablename__ = 'menu_daughter'
    id: Mapped  [int] = mapped_column(primary_key=True)
    tittlenamemenu: Mapped [str]
    labale: Mapped [str] = mapped_column(ForeignKey("menu_parents.labale", ondelete="CASCADE"))
    daughter: Mapped [str]



