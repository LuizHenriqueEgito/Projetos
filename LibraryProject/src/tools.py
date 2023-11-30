# crie as funções que adiciona livros, empresta e calcula a multa
from database.crud import (
    add_row,
    select_id_book,
    select_id_client,
    add_rent_table,
    select_client_delay,
    update_client,
    select_client
)
from database.database import Book, Client
from functools import partial
from datetime import datetime, timedelta


add_client_ = partial(add_row, table=Client)
add_book_ = partial(add_row, table=Book)

def add_client():
    client_name = str(input('Client name: '))
    kwargs = {
        'client_name': client_name,
        'delay_ticket': 0
    }
    return add_client_(**kwargs)

def add_book():
    book_name = str(input('Book name: '))
    gender = str(input('gender: '))
    n_pages = int(input('pags: '))
    kwargs = {
        'book_name': book_name,
        'gender': gender,
        'n_pages': n_pages
    }
    return add_book_(**kwargs)

def rent_book(client: str, book: str, days_devolution: datetime):
    # TODO: Essa função vincula uma pessoa a um livro e salva na base rent
    id_book = select_id_book(book_name=book)
    id_client = select_id_client(client_name=client)
    dt_today = datetime.now()
    dt_devolution = dt_today + timedelta(days=days_devolution)
    kwargs = {
        'client_id': id_client,
        'book_id': id_book,
        'dt_rent': dt_today,
        'dt_devolution': dt_devolution,
        'returned': False,
        'days_delay': 0
        }
    return add_rent_table(**kwargs)


def apply_delay_ticket(ticket: float = 3.) -> None:
    # TODO: Essa função identifica pessoas com delay na devolução e aplica a elas a multa
    # TODO: query na rent, atualiza e printa
    # faça um select no tabela rent busque quem está com o days delay
    # pegue o tempo de days delay e multiplique pela multa e insira na tabela client em delay _ticket
    ids_list = select_client_delay()
    for client in ids_list:
        ticket_value = client[1] * ticket
        update_client(
            client_id=client[0],
            values_dict={'delay_ticket': ticket_value}
            )


def summary_client(client_id: int):
    # TODO: essa função ve o status do client e diz se ele pode ou não pegar mais livros 
    dict_client = select_client(client_id=client_id)
    condition = any(value <= 0 for value in dict_client.values())
    client, *_ = dict_client
    ticket = dict_client[client]
    if condition:
        print(f'O cliente {client} pode pegar novos livros.')
    else:
        print(f'O cliente {client} precisa pagar R$ {ticket} para pegar novos livros.')



if __name__ == '__main__':
    # client = {'client_name': 'Luiz', 'delay_ticket': 0}
    # book = {'book_name': 'Matrix I', 'gender': 'Action', 'n_pages': 980}
    # add_client(**client)
    # add_book(**book)
    # rent_book(client='Luiz', book='Matrix I', days_devolution=7)
    # apply_delay_ticket(ticket=7.)
    summary_client(client_id=3)
