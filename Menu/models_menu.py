from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


"""import enum
#Если необходимо создать список установленных параметров 
class WorkSection (enum.Enum):
    parameter_1 = values_1
    parameter_2 = values_2
    
    а в дата классе указываем как
    work_section: Mapped [WorkSection]
    
"""

class MenuParents(Base):
    __tablename__ = 'menu_parents'
    id: Mapped  [int] = mapped_column(primary_key=True)
    tittlenamemenu: Mapped [str]
    labale: Mapped [str]
    parent: Mapped [str]
    description: Mapped [str]
    iswork: Mapped [bool]

class MenuDaughter(Base):
    __tablename__ = 'menu_daughter'
    id: Mapped  [int] = mapped_column(primary_key=True)
    tittlenamemenu: Mapped [str]
    labale: Mapped [str] = mapped_column(ForeignKey("menu_parents.labale", ondelete="CASCADE"))
    daughter: Mapped [str]
    daughter_tittlenamemenu: Mapped [str] = mapped_column(nullable=True)
    description: Mapped[str]
    iswork: Mapped[bool]

class MenuUser(Base):
    __tablename__ = 'menu_user'
    id: Mapped  [int] = mapped_column(primary_key=True)
    user_id: Mapped [str]
    user_name: Mapped [str]
    user_name_id: Mapped [str]
    tittlenamemenu_choised: Mapped [str]


def create_table_class(table_name):
    class DynamicTable(Base):
        __tablename__ = table_name
        id: Mapped  [int] = mapped_column(primary_key=True)
        user_id: Mapped [str]
        user_name: Mapped [str]
        english_word: Mapped [str]
        russian_word: Mapped [str]
        know_word: Mapped [str]
        mistake: Mapped [str]
    return DynamicTable