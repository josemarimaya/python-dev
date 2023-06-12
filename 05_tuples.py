## TUPLAS ##

# Operadores de creación de tuplas

my_tuple = tuple()
other_tuple = ()

my_tuple = (27, 1.75, "Josemari", "Maya")

# A priori hay muchas operaciones similares con las de las listas

# index cambia devolviéndote el index en el que se encuentra el valor que le pasas
print(my_tuple.index(27))

""" La diferencia general entra las tuplas y las listas es que las tuplas son
    colecciones inmutables con lo cual no podremos modificar ningún valor una vez añadido originalmente"""

# Podemos transformas un tupla en una lista tal que podamos modificar algún valor

my_tuple = list(my_tuple)

my_tuple.append("Rojo")

print(my_tuple)

my_tuple = tuple(my_tuple)

print(type(my_tuple))