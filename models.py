from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base, str_200
from typing import Optional
import enum

class Worker(Base):
    __tablename__ = 'workers'
    id: Mapped  [int] = mapped_column(primary_key=True)
    username: Mapped [str]

class Workload (enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"

class ResumeOrm(Base):
    __tablename__ = 'resumes'
    id: Mapped  [int] = mapped_column(primary_key=True)
    title: Mapped [str_200]
    compensation: Mapped [Optional [int]]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))


class UserTable(Base):
    __tablename__ = 'userTable'
    id: Mapped  [int] = mapped_column(primary_key=True)
    firstname: Mapped [str_200]
    secondname: Mapped [str_200]


"""metadata_obj = MetaData()
worker_table = Table (
    'workers',
    metadata_obj,
    Column ('id', Integer, primary_key=True),
    Column ('username', String)
)
"""