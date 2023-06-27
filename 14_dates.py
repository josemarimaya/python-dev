## FECHAS ##

from datetime import datetime

# Inicializamos un objeto de tipo date
now = datetime.now()

print(now)

# Llamadas a distintas funciones de date
print(now.hour)
print(now.year)

timestamp = now.timestamp()

print(timestamp)

summer = datetime(2023, 6, 23)


def print_date(fecha):
    print(fecha.year)
    print(fecha.month)
    print(fecha.day)
    print(fecha.hour)
    print(fecha.minute)
    print(fecha.second)


print_date(now)

print(summer)

today_now = datetime.now()

print(today_now)

# Paque que nos permite operar con fechas

from datetime import timedelta

start_td = timedelta(200, 100, 100, weeks=20)
end_td = timedelta(300, 100, 100, weeks=30)

# Sobre todo su utilidad es para trabajar con franjas de horarios

print(end_td - start_td)
print(end_td + start_td)
print(end_td / start_td)
