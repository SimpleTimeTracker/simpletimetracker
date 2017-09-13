import source.jsonpickle as jsonpickle

def _checkDbName(db, name):
    for i in range(len(db)):
        if db[i].name == name:
            return i
    return "ERROR"

def _loadDb(fp):
    null = []
    text = fp.read()
    try:
        return jsonpickle.decode(text)
    except:
        return null

def deleteProject(db, name):
    i = _checkDbName(db, name)
    if i == "ERROR":
        print "Error in the name of the project. Retry"
        exit()
    del db[i]

def getLastStarted(db, name):
    i = _checkDbName(db, name)

    if i == "ERROR":
        print "Error in the name of the project. Retry"
        exit()

    length = len(db[i].sessions)
    try:
        session = db[i].sessions[length - 1]
    except IndexError:
        print "Error: There isn't time started to stop in this project."
        exit()

    if session.time_start == [] or session.time_end != []:
        print "Error: There isn't time started to stop in this project."
        exit()

    return session

def getProject(db, name):
    i = _checkDbName(db, name)

    if i == "ERROR":
        print "Error in the name of the project. Retry"
        exit()

    return db[i]



def closing(db):
    fp = open("source/db_001.json", "w")
    fp.write(jsonpickle.encode(db))
    fp.close()
