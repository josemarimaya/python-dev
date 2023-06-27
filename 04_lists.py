### LISTAS ###

ls = []  # Forma clásica de invocar una lista vacía
my_list = list()  # Lista vacía inicializada por función, ambas opciones son igual de válidas

# Podemos usar las funciones que tiene propiamente el sistema como anteriormente lo hemos hecho

print(len(ls))

my_list = [27, 30, 15, 3, 5, 15, 27, 5, 15, 5]

print(my_list)

ls = [27, 1.77, "Josemari", "Maya"]

""" Podemos acceder a los valores de una lista de la misma manera
    que lo hicimos con los strings"""
print(ls[0])  # Acceso a los valores
print(ls[-2])  # Devolveremos el valor en la posición (len(ls) - 2)
# print(ls[-5]) # Evidentemente no podemos acceder a las posiciones que no existen en la lista IndexError

print(type(ls))  # Vemos el tipo de la variable, en este caso es lista

# Count, no cuenta los valores que hay en la lista sino cuantas veces está repetido el valor que le pasas por parametro
print(my_list.count(5))

print(len(my_list))  # len(lista) es lo que se usa para ver cuantos parametros hay en la lista

# Asignamos nombre de variables a los valores de la lista, los nombres se relacionan según el orden indexado a la lista
# Es mala práctica reasignar los valores indexandolos con otro orden directamente
age, height, name, surname = ls

print(surname)

# Para concatenar ambas listas añadimos un más para crear una lista con las dos o pasarla por pantalla
ambas_listas = ls + my_list

print(ambas_listas)

""" Recordamos que las variables que usamos son globales y el tipado es dinámico
    con lo cual si cambiamos el valor a la variable esta se actualiza con el
                        ÚLTIMO VALOR QUE SE LE HA DADO"""

# Append pone al final de la lista los valores que le pasamos
ls.append("Rojo")
ls.append("Negro")
print(ls)

# Con insert le indicamos la posición en la que queremos añadir un valor
ls.insert(4, "Cano")
print(ls)

# Podemos copiar la lista en una var nueva para que no se pierda la lista ahora mismo

copy_list = ls.copy()

# Remove borra el valor que se le mete como parámetro
# NO se puede meter un índice con remove
ls.remove("Negro")
print(ls)

# Con pop() sin parametro desapilamos o quitamos el último valor de la lista
ls.pop()
print(ls)

# Si le pasamos a un print la función de pop únicamente vemos el valor que se va a desapilar y se ejecuta la función

print(ls.pop())
print(ls)

# También podemos popear un elemento y guardarlo en una variable al mismo tiempo
elemento_popeado = ls.pop(2)
print(ls)
print(elemento_popeado)

# Así podemos eliminar el valor de una posición directamente
del ls[2]
print(ls)

edad = ls[0]
# Podemos indexar un valor directamente en la lista, sobrescribiendo la que hay en esa posición
ls[0] = "Josemari Maya"
print(ls)

ls.insert(2, edad)
print(ls)

# Comprobamos que la lista copiada se mantiene igual a la que estaba originalmente
print(copy_list)

"""Tanto como sort como reverse tienen que ejecutarse antes de que se haga el print
    porque sino no devuelve ningún tipo de valor"""

# Damos la vuelta a la lista

copy_list.reverse()

print(copy_list)

""" Podemos ordenar la listas usando la función .sort() que a priori si estamos usando Integer los ordenará
    de menor a mayor y si son string los ordenará por orden alfabético"""

ml = [5, 4, 10, 9, 25]
ml.sort()
print(ml)

print(ls)

# Creación de sublistas

# En general podemos usar los índices que usamos en el apartado de strings
print(ml)
ml_slice = ml[0:3]
print(ml_slice)

import random

ciudades = ["Sevilla", "Cadiz", "Malaga", "Huelva", "Almeria", "Jaen", "Cordoba"]


def genera_permutacion_inversa(lista_ciudades):
    numero_ciudades = len(lista_ciudades)

    ciudad_1 = random.choice(range(0, numero_ciudades))
    print(lista_ciudades[ciudad_1])
    ciudad_2 = random.choice(range(0, numero_ciudades))
    print(lista_ciudades[ciudad_2])
    nueva_lista = lista_ciudades[ciudad_1::-1] + lista_ciudades[ciudad_2::-1]

    ciudades_set = set(nueva_lista)
    return nueva_lista, ciudades_set


print(genera_permutacion_inversa(ciudades))
