# Biblioteca

- Crie 3 tabelas:
    - [x] Book (id, book_name, gender, n_pages)
    - [x] Client (id, client_name, delay_ticket)
    - [x] Rent (id, client_id, book_id, dt_rent, dt_devolution, returned, days_delay)
- [x] Cadastre pessoas e livros
- O emprestimo dura `n` dias
- Existe a opção de renovar
- Se o livro não for entregue no dia nem renovado comece a incorrer a multa de R$ `x,00`
- A cada cadastramento tudo e rerodado
- 1 cliente pode pegar `n` livros