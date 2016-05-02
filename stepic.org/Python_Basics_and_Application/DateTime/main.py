import datetime
def wrapper(value):
    return str(int(value))
(year, month, day) = input().split(' ')
days = int(input())
date_delta = datetime.timedelta(days=days)
date_origin = datetime.date(int(year), int(month), int(day))
date_new = date_origin + date_delta
date_print = date_new.strftime('%Y %m %d').split(' ')
print(wrapper(date_print[0]) + ' ' + wrapper(date_print[1]) + ' ' + wrapper(date_print[2]))