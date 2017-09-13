def projectExport(obj, pricePerH):
    namefile = 'Export/' + obj.name + '_export.txt'
    fp = open(namefile, "w")
    fp.write(obj.name + '\n\n')
    fp.write("SESSIONS:\n")
    fp.write("STARTED\t\t\tENDED\t\t\tTIME WORKED\n")
    for el in obj.sessions[1:]:
        fp.write(_create_string(el))
    fp.write("\nTOTAL WORKED: ")
    fp.write(_string_worked(_get_total_worked(obj.sessions)))
    if pricePerH != 0:
        fp.write("\nTOTAL PRICE: %.2f" % _get_cash(_get_total_worked(obj.sessions), pricePerH))
    fp.close()

def _create_string(obj):
    string = ''
    string += _string_date(obj.time_start) + \
                _string_hour(obj.time_start) + \
                _string_date(obj.time_end) + \
                _string_hour(obj.time_end) + \
                _string_worked(obj.time_worked) + '\n'
    return string

def _string_date(obj):
    string = ''
    for el in obj[:2]:
        string += (str(el).zfill(2) + '/')
    string += (str(obj[2]).zfill(2) + '  ')
    return string

def _string_hour(obj):
    string = ''
    string += (str(obj[3]).zfill(2)+':'+str(obj[4]).zfill(2)+'       ')
    return string

def _string_worked(obj):
    string = ''
    flag = 0
    i = 0
    for el in obj:
        if el != 0 or flag == 1:
            string += (str(el) + ' ')
            if i == 0:
                string += 'Years '
                flag = 1
            elif i == 1:
                string += 'Months '
                flag = 1
            elif i == 2:
                string += 'Days '
                flag = 1
            elif i == 3:
                string += 'Hours '
                flag = 1
            elif i == 4:
                string += 'Mins '
                flag = 1
            elif i == 5:
                string += 'Secs '
                flag = 1
        i += 1
    return string

def _get_total_worked(obj):
    flag = 0
    total = [0, 0, 0, 0, 0, 0]
    for el in obj[1:]:
        for i in range(6):
            total[i] += el.time_worked[i]
    while flag == 0:
        flag = 1
        for i in reversed(range(6)):
            if i == 4 or i == 5:
                if total[i] >= 60:
                    total[i] -= 60
                    total[i-1] += 1
                    flag = 0
            elif i == 3:
                if total[i] >= 24:
                    total[i] -= 24
                    total[i-1] += 1
                    flag = 0
            elif i == 2:
                if total[i] >= 30:
                    total[i] -= 30
                    total[i-1] += 1
                    flag = 0
            elif i == 1:
                if total[i] >= 12:
                    total[i] -= 12
                    total[i-1] += 1
                    flag = 0
    return total

def _get_cash(obj, pricePerH):
    cash = 0
    hours = ((obj[0]*8760) + (obj[1]) * 720) + (obj[2] * 24) + (obj[3])
    cash += hours * pricePerH
    secs = ((obj[4] * 60) + obj[5])
    cash += secs * (pricePerH/3600)
    return cash
