from __future__ import print_function

def printList(db):
    for obj in db:
        print(obj.name)

def printSessions(project):
    print("STARTED", end='\t\t\t')
    print("ENDED", end='\t\t\t')
    print("TIME WORKED", end='\n')
    for obj in project.sessions:
        _print_date(obj.time_start)
        _print_hour(obj.time_start)
        print("\t", end='')
        _print_date(obj.time_end)
        _print_hour(obj.time_end)
        print("\t", end='')
        _print_worked_str(obj.time_worked)

def _print_date(obj):
    for i in range(2):
        print(obj[i], end='/')
    print(obj[2], end=' ')

def _print_hour(obj):
    print(str(obj[3]).zfill(2), end=':')
    print(str(obj[4]).zfill(2), end=' ')

def _print_worked_str(obj):
    flag = 0
    i = 0
    for el in obj:
        if el != 0 or flag == 1:
            print(el, end=' ')
            if i == 0:
                print('Years ', end='')
                flag = 1
            elif i == 1:
                print('Months ', end='')
                flag = 1
            elif i == 2:
                print('Days', end='')
                flag = 1
            elif i == 3:
                print('Hours ', end='')
                flag = 1
            elif i == 4:
                print('Mins ', end='')
                flag = 1
            elif i == 5:
                print('Secs ', end='\n')
                flag = 1
        i += 1

def printWorked(session):
    flag = 0
    print("You worked:", end=' ')
    for i in range(6):
        if session.time_worked[i] != 0 or flag == 1:
            print(str(session.time_worked[i]) + ' ', end='')
            if i == 0:
                print('Years ', end='')
                flag = 1
            elif i == 1:
                print('Months ', end='')
                flag = 1
            elif i == 2:
                print('Days', end='')
                flag = 1
            elif i == 3:
                print('Hours ', end='')
                flag = 1
            elif i == 4:
                print('Mins ', end='')
                flag = 1
            elif i == 5:
                print('Secs ', end='\n')
                flag = 1
