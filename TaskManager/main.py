from src.utils import do_task, summary


if __name__ == "__main__":
    while True:
        print('Choice the option:')
        print('[1] add task')
        print('[2] summary')
        print('[3] Exit')
        optinion = int(input('Opition: '))
        if optinion == 1:
            task = str(input('Input task: '))
            timer = int(input('Timer: '))
            do_task(task=task, minutes=timer)
        if optinion == 2:
            days = int(input('Days: '))
            summary(days=days)
        if optinion == 3:
            break
