from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class DictionaryEngRus(Base):
    __tablename__ = 'dictionary_eng_rus'
    id: Mapped  [int] = mapped_column(primary_key=True)
    english_word: Mapped [str]
    russian_word: Mapped [str]
    exemple_use: Mapped [str]
