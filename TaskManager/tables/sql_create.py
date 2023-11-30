import datetime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, DateTime, Integer
from sqlalchemy.sql import func
from tables.connection import connection

class Base(DeclarativeBase):
    pass

class TableDoing(Base):
    __tablename__ = 'table_do'
    id: Mapped[int] = mapped_column(primary_key=True)
    task: Mapped[str] = mapped_column(String(30))
    timer: Mapped[int] = mapped_column(Integer)
    finish: Mapped[int] = mapped_column(Integer, default=0)  # atualize na tabela comece com 0 quando finalizar flag 1
    dt_insertion: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
        )

def initialize_tables(conn=connection):
    Base.metadata.create_all(conn)

if __name__ == '__main__':
    initialize_tables()