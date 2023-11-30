# crie o menu da biblioteca aqui
from src.tools import (
    add_client,
    add_book,
    rent_book,
    summary_client,
)


if __name__ == '__main__':
    print('Bem vindo a Biblioteca L&M')
    while True:
        print("""
        [1]: Add new client;
        [2]: Rent book;
        [3]: Summary client;
        [4]: Add new book;
        """)
        option = int(input('Escolha sua opção: '))
        if option == 1:
            add_client()
        if option == 2:
            client = str(input('Client name: '))
            book = str(input('Book: '))
            days_devolution = int(input('Days to Devolution: '))
            rent_book(
                client=client,
                book=book,
                days_devolution=days_devolution
                )
        if option == 3:
            client_id = int(input('Client Id: '))
            summary_client(client_id=client_id)
        if option == 4:
            add_book()