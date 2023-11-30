from sqlalchemy.orm import Session
from tables.connection import engine
from tables.sql_create import TableDoing
from sqlalchemy import select, update, func, desc
from datetime import datetime, timedelta


def update_finish(finish: int = 1):
    with Session(engine) as session:
        # pegando o ultimo ID
        last_id = (
            session.query(func.max(TableDoing.id))
            .scalar()
        )
        stmt = (
            update(TableDoing).
            where(TableDoing.id == last_id).
            values(finish=finish)
        )
        # atualizando a tabela
        session.execute(stmt)
        session.commit()

def update_not_finished(timer: int):
    with Session(engine) as session:
        query_timer_id = (
            session.query(TableDoing.id, TableDoing.timer)
            .order_by(desc(TableDoing.id))
            .limit(1)
        )
        for row in query_timer_id:
            id_, timer_initial = row
        timer += timer_initial
        stmt = (
            update(TableDoing).
            where(TableDoing.id == id_).
            values(timer=timer)
        )
        session.execute(stmt)
        session.commit()


def delta_date(days):
    # Obtém a data e hora atual
    data_hora_atual = datetime.now()
    # Calcula a diferença de tempo de 'days' days atrás
    delta = timedelta(days=days)
    # Subtrai o delta da data e hora atual para obter a data e hora desejadas
    dt_summary_filter  = data_hora_atual - delta
    return dt_summary_filter


def insert_task_do(task: str, timer: int):
    with Session(engine) as session:
        task_test = TableDoing(
            task=task,
            timer=timer
        )
        session.add_all([task_test])
        session.commit()

def query(days=0):
    if days:
        format_datetime = delta_date(days=days)
        stmt = (
            select(TableDoing)
            .where(TableDoing.dt_insertion >= format_datetime)
            .order_by(TableDoing.dt_insertion.asc())
        )
    else:
        stmt = (
            select(TableDoing)
            .order_by(TableDoing.dt_insertion.asc())
        )
    query_result = []
    with engine.connect() as conn:
        for row in conn.execute(stmt):
            query_result.append(row)
    return query_result


if __name__ == '__main__':
    # query_ = query(1)
    _ = query(days=0)
    # update_table(finish=1)


