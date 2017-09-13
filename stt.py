"""Usage:
    stt.py -h | --help | --version
    stt.py list
    stt.py newproject <project>
    stt.py deleteproject <project>
    stt.py start <project>
    stt.py stop <project>
    stt.py export <project> [-p VALUE]
    stt.py <project>

Options:
    -p --price      your price per hour
"""
import atexit

from docopt import docopt
from source.db_def import _loadDb, deleteProject, getLastStarted, getProject, closing
from source.print_def import printList, printSessions, printWorked
from source.classes import Project, Session


if __name__ == '__main__':
    ARGUMENTS = docopt(__doc__, version='1.0.0rc')

try:
    FP = open("source/db_001.json")
    DB = _loadDb(FP)
    FP.close()
except IOError:
    DB = []

if ARGUMENTS['list']:
    printList(DB)

elif ARGUMENTS['newproject']:
    NEWPROJECT = Project()
    NEWPROJECT.add_project(DB, ARGUMENTS['<project>'])

elif ARGUMENTS['deleteproject']:
    deleteProject(DB, ARGUMENTS['<project>'])

elif ARGUMENTS['start']:
    NEWSESSION = Session()
    NEWSESSION.get_time_start(DB, ARGUMENTS['<project>'])

elif ARGUMENTS['stop']:
    SESSION = getLastStarted(DB, ARGUMENTS['<project>'])
    SESSION.get_time_end_n_worked()
    printWorked(SESSION)

elif ARGUMENTS['export']:
    PROJECT = getProject(DB, ARGUMENTS['<project>'])
    PROJECT.export_project(ARGUMENTS['VALUE'])

else:
    PROJECT = getProject(DB, ARGUMENTS['<project>'])
    printSessions(PROJECT)


atexit.register(closing, DB)
