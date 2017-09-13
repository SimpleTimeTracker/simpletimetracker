def _checkDbName(db, name):
    for i in range(len(db)):
        if db[i].name == name:
            return i
    return "ERROR"
