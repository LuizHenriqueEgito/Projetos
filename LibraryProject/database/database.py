# Crie as tabelas aqui (crie as funções de Drop também)
from typing import Optional
from datetime import datetime
from sqlmodel import Field, Field, Session, SQLModel, create_engine

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    book_name: str
    gender: str
    n_pages: Optional[int] = Field(default=0)


class Client(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    client_name: str
    delay_ticket: int = Field(default=0)


class Rent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    client_id: int = Field(foreign_key='client.id')
    book_id: int = Field(foreign_key='book.id')
    dt_rent: datetime = Field(default_factory=datetime.utcnow)
    dt_devolution: datetime = Field(default_factory=datetime.utcnow)
    returned: bool = Field(default=True)
    days_delay: int


def drop_table(table):
    table.drop(engine)


engine = create_engine("sqlite:///database/database.db")

    
if __name__ == '__main__':
    # Create all tables
    SQLModel.metadata.create_all(engine)