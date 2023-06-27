## COMPRESION DE LISTAS ##

my_list = [27, 30, 15, 3, 5, 15, 27, 5, 15, 5]

""" La compresión de listas no permite trabajar y mutar la lista original directamente
    usando un for dentro de la misma e iterando tal como lo haríamos fuera"""

other_list = [i for i in my_list]

# Hemos copiado la lista porque lo único que hemos hecho ha sido añadirle cada i de la original
print(other_list)

other_list = [i - 5 for i in other_list]

print(other_list)

range_list = [i for i in range(15)]

print(range_list)