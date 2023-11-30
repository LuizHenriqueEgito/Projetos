from tables.sql_create import TableDoing
from tables.connection import engine

def drop_table():
    TableDoing.__table__.drop(engine)