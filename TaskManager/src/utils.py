from time import sleep
from src.alert import alarme
from tables.orm import query, update_finish, insert_task_do, update_not_finished
from prettytable import PrettyTable


def temporizador(task: str, minutes: int):
    for minute in range(minutes, 0, -1):
        print(
            f'Task: {task} \t\t | \t\t Timer: {minute}'.ljust(30),
            end='\r'
            )
        sleep(60)


def do_task(task: str, minutes: int, insert_task: bool = True):
    temporizador(task=task, minutes=minutes)
    if insert_task:
        insert_task_do(task=task, timer=minutes)
    print("Time is over")
    alarme() 
    while True:
        finish = str(input('Task finish [y/n]: '))
        finish = 1 if finish == 'y' else 0
        if finish:
            update_finish(finish=finish)
            return None
        else:
            flag_continue = str(input('Continuar: [y/n]'))
            flag_continue = 1 if finish == 'y' else 0
            if flag_continue:
                new_timer = int(input('Timer: '))
                update_not_finished(timer=new_timer)
                temporizador(task=task, minutes=new_timer)
            else:
                return None


def summary(days: int = 0):
    query_ = query(days=days)
    table = PrettyTable()
    table.field_names = ["task", "timer", "finish", "dt_inserção"]
    for row in query_:
        table.add_row(row[1:])
    print(table)