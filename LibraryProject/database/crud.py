# Crie as funções de insert, update e delete aqui
from typing import Dict, Union, List, Tuple
from datetime import datetime, timedelta
from functools import partial
from sqlmodel import Session, update, create_engine, select
from faker import Faker

from database.database import Book, Client, Rent

engine = create_engine("sqlite:///database/database.db")



def select_client_delay() -> List[Tuple[int, int]]:
    with Session(engine) as session:
        stmt = (
        select(Client.id, Client.client_name, Rent.client_id, Rent.days_delay)
        .join(Rent, Client.id == Rent.client_id)
        .where(Rent.days_delay > 0)
        )
        results = session.exec(stmt)
        clients_ids = []
        for row in results:
            values = (row[0], row[-1])
            clients_ids.append(values)  # pega o id e o tempo de atraso
            print(f'valus: {values}')
    return clients_ids

def select_client(client_id: int) -> Dict[str, float]:
    with Session(engine) as session:
        stmt = (
            select(Client.client_name, Client.delay_ticket)
            .where(Client.id == client_id)
        )
        result = session.exec(stmt).one_or_none()

        if result:
            client_name, delay_ticket = result
            return {client_name: delay_ticket}
        else:
            return {}


def update_rent():
    ...

def select_id_book(book_name: str):
    with Session(engine) as session:
        stmt = select(Book.id).where(Book.book_name == book_name)
        results = session.exec(stmt).one()
    return results


def select_id_client(client_name: str):
    with Session(engine) as session:
        stmt = select(Client.id).where(Client.client_name == client_name)
        results = session.exec(stmt).one()
    return results


def add_row(table, **kwargs):
    with Session(engine) as session:
        row = table(**kwargs)
        session.add(row)
        session.commit()

def rm_row(table, id: int):
    with Session(engine) as session:
        stmt = select(table).where(table.id == id)
        result = session.exec(stmt)
        row = result.one()
        session.delete(row)
        session.commit()

def update_book(book_name: str, values_dict: Dict[str, Union[str, float, int]]):
    table = Book
    with Session(engine) as session:
        stmt = select(table).where(table.book_name == book_name).limit(1)
        book = session.exec(stmt).first()

        if book:
            for key, value in values_dict.items():
                setattr(book, key, value)

            session.commit()
            session.refresh(book)

            return book
        else:
            return None

def update_client(
        client_id: str,
        values_dict: Dict[str, Union[str, float, int]]
):
    table = Client
    with Session(engine) as session:
        stmt = select(table).where(table.id == client_id).limit(1)
        client = session.exec(stmt).first()

        if client:
            for key, value in values_dict.items():
                # setattr(client, key, (client.n_rented_books + 1))
                setattr(client, key, value)
            
            session.commit()
            session.refresh(client)

            return client
        else:
            return None

def update_client_n_rented_books(
        client_id: str,
        values_dict: Dict[str, Union[str, float, int]]
):
    table = Client
    with Session(engine) as session:
        stmt = select(table).where(table.id == client_id).limit(1)
        client = session.exec(stmt).first()

        if client:
            for key, value in values_dict.items():
                setattr(client, key, (client.n_rented_books + 1))
            
            session.commit()
            session.refresh(client)

            return client
        else:
            return None

def add_rent_table(**kwargs):
    with Session(engine) as session:
        row = Rent(**kwargs)
        session.add(row)
        session.commit()


if __name__ == '__main__':
    # id_book = select_id_book(book_name='camera')
    # print(id_book)
    # id_client = select_id_client(client_name='Luiz')
    # print(id_client)
    # rm_row(table=Book, id=3)
    # update_book(book_name='livro', values_dict={'generous': 'Comedy'})
    a = select_client_delay()