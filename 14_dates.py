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
