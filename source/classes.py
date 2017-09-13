
from __future__ import print_function
from source.time_def import getTime, _checkTimeWorked
from source import jsonpickle
from source.db_def import _checkDbName
from source.export_def import projectExport

class Project():
    name = ''
    sessions = []

    """To add a project in the database"""
    def add_project(self, db, name):
        i = _checkDbName(db, name)
        if i != "ERROR":
            print("Error, the project already exists. Retry")
        else:
            self.name = name
            self.sessions = []
            db.append(self)

    """To export a project in the Export folder"""
    def export_project(self, price):
        if price == None:
            price = 0
        stringPrice = ""
        try:
            floatPrice = float(price)
            projectExport(self, floatPrice)
        except:
            for c in price:
                if c == ',':
                    c = '.'
                stringPrice += c
            projectExport(self, float(stringPrice))

class Session():
    time_start = []
    time_end = []
    time_worked = []

    """Assign time_start to current time"""
    def get_time_start(self, db, name):
        i = _checkDbName(db, name)
        if i == "ERROR":
            print("Error in the name of the project. Retry")
        else:
            self.time_start = getTime()
            self.time_end = []
            self.time_worked = []
            db[i].sessions.append(self)

    """Assign time_end and calculate time_worked"""
    def get_time_end_n_worked(self):
        self.time_end = getTime()
        for i in range(6):
            dif = self.time_end[i] - self.time_start[i]
            self.time_worked.append(dif)
        _checkTimeWorked(self)
