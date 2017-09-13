import time

def getTime():
    now = time.localtime()
    val = []
    for i in range(6):
        val.append(now[i])
    return val

def _checkTimeWorked(obj):
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
