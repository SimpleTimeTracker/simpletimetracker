from __future__ import print_function
import time
from source import jsonpickle


class Project():
    name = ''
    sessions = []

class Session():
    time_start = []
    time_end = []
    time_worked = []

def _get_time():
    now = time.localtime()
    val = []
    for i in range(6):
        val.append(now[i])
    return val

def _load_db(fp):
    null = []
    text = fp.read()
    try:
        return jsonpickle.decode(text)
    except:
        return null

def _print_worked(obj):
    print("You worked: ", end='')
    flag = 0
    for i in range(6):
        dif=obj.time_end[i] - obj.time_start[i]
        obj.time_worked.append(dif)
    _check_worked(obj)
    for i in range(6):
        if obj.time_worked[i] != 0 or flag == 1:
            print(str(obj.time_worked[i]) + ' ', end= '')
            if i == 0:
                print('Years ', end='')
                flag = 1
            elif i==1:
                print('Months ', end='')
                flag = 1
            elif i==2:
                print('Days', end='')
                flag = 1
            elif i==3:
                print('Hours ', end='')
                flag = 1
            elif i==4:
                print('Mins ', end='')
                flag = 1
            elif i==5:
                print('Secs ', end='\n')
                flag = 1


def _print_list(db):
    for obj in db:
        print(obj.name)

def _check_db_name(db, string):
    for i in range(len(db)):
        if db[i].name == string:
            return i
    return "ERROR"

def _check_worked(obj):
    flag = 0
    worked = obj.time_worked
    while flag == 0:
        flag = 1
        for i in reversed(range(6)):
            if i == 4 or i == 5:
                if worked[i] < 0:
                    worked[i] += 60
                    worked[i-1] -= 1
                    flag = 0

            elif i == 3:
                if worked[i] < 0:
                    worked[i] += 24
                    worked[i-1] -= 1
                    flag = 0

            elif i == 2:
                if worked[i] < 0:
                    worked[i] += 30
                    worked[i-1] -= 1
                    flag =  0

            elif i == 1:
                if worked[i] < 0:
                    worked[i] += 12
                    worked[i-1] -= 1
                    flag = 0
    obj.time_worked=worked


def _new_project(db, command):
    string = command[11:len(command)]
    if string == "":
        print("Error, the name of the project cannot be empty. Retry")
    new_project = Project()
    new_project.name = string
    new_project.sessions = [Session()]
    db.append(new_project)

def _print_sessions(db, index):
    print("STARTED", end='\t\t\t')
    print("ENDED", end='\t\t\t')
    print("TIME WORKED", end='\n')
    for obj in db[index].sessions[1:]:
        _print_date(obj.time_start)
        _print_hour(obj.time_start)
        print("\t\t", end='')
        _print_date(obj.time_end)
        _print_hour(obj.time_end)
        print("\t\t", end='')
        _print_worked_str(obj.time_worked)

def _print_date(obj):
    for i in range(2):
        print(obj[i], end='/')
    print(obj[2], end= ' ')

def _print_hour(obj):
    print(str(obj[3]).zfill(2), end=':')
    print(str(obj[4]).zfill(2), end= ' ')

def _print_worked_str(obj):
    flag = 0
    i=0
    for el in obj:
        if el != 0 or flag == 1:
            print(el, end = ' ')
            if i == 0:
                print('Years ', end='')
                flag = 1
            elif i==1:
                print('Months ', end='')
                flag = 1
            elif i==2:
                print('Days', end='')
                flag = 1
            elif i==3:
                print('Hours ', end='')
                flag = 1
            elif i==4:
                print('Mins ', end='')
                flag = 1
            elif i==5:
                print('Secs ', end='\n')
                flag = 1
        i+=1


def _closing(obj):
    fp=open("source/db_001.json", "w")
    fp.write(jsonpickle.encode(obj))
    fp.close()
