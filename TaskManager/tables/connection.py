from sqlalchemy import create_engine

# Substitua "sqlite:///mydatabase.db" pelo caminho e nome do arquivo do seu banco de dados SQLite.
engine = create_engine('sqlite:///tables/taskmanager.db')

# Conecta ao banco de dados
connection = engine.connect()