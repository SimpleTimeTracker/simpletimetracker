from __future__ import print_function
from source import classes
from source import export_def as exp
import atexit

START = "------SIMPLE TIME TRACKER------\nTYPE \"help\" IF YOU NEED"
help_file = open("doc/help.txt")
HELP = help_file.read()
help_file.close()

try:
    fp=open("source/db_001.json")
    db = classes._load_db(fp)
    fp.close()
except:
    db = []

print(START)
print("Active Projects: " + str(len(db)))
command = ''
while command != 'quit':
    command=raw_input("\nInsert the command: ")
    if command == 'list':
        classes._print_list(db)

    elif command == 'help':
        print(HELP)

    elif command[:11] == "newproject ":
        i = classes._check_db_name(db, command[11:len(command)])
        if i != "ERROR":
            print("Error, the project already exists. Retry")
            continue
        classes._new_project(db, command)

    elif command[:14] == "deleteproject ":
        i = classes._check_db_name(db, command[14:len(command)])
        if i == "ERROR":
            print("Error in the name of the project. Retry")
            continue
        while True:
            choose = raw_input("Do you really want to delete the project? (y/n): ")
            if choose == 'n':
                break
            elif choose == 'y':
                del db[i]
            else:
                print("Please insert y as yes or n as no.")
            break

    elif command[:6] == 'start ':
        i = classes._check_db_name(db, command[6:len(command)])
        if i == "ERROR":
            print("Error in the name of the project. Retry")
            continue
        project = classes.Project()
        session = classes.Session()
        session.time_start = classes._get_time()
        session.time_worked = []
        while command != 'stop':
            command = raw_input("Well done, return here when you finish your job to stop me...\n")
            if command == 'stop':
                session.time_end = classes._get_time()
                classes._print_worked(session)
                db[i].sessions.append(session)

    elif command[:7] == 'export ':
        i = classes._check_db_name(db, command[7:len(command)])
        if i == "ERROR":
            print("Error in the name of the project. Retry")
            continue
        while True:
            choose = raw_input("Do you want to calculate the total price(y/n): ")
            if choose == 'n':
                exp._project_export(db[i], 0)
                break
            elif choose == 'y':
                while True:
                    try:
                        pricePerH = int(raw_input("Insert your price per hour: "))
                    except:
                        print("Invalid number, try again.")
                        continue
                    exp._project_export(db[i], pricePerH)
                    break
            else:
                print("Please insert y as yes or n as no.")
            break

    elif command != 'quit':
        i = classes._check_db_name(db, command)
        if i == "ERROR":
            print("Error in the name of the project. Retry")
            continue
        classes._print_sessions(db, i)

g = atexit.register(classes._closing, db)
