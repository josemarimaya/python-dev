## SETS ##

# La llamada al constructor del set es la misma que la del dict por ello si está vacío aparecerá como dict
my_set = set()
other_set = {}

print(type(other_set))

""" Al ser python un lenguaje de tipado dinámico hasta que no definimos 
    que únicamente se repite una vez cada valor no pasa a Set.
    
    Ya que la definición de Set es que cada valor se repite una sola vez.
    
    Además, de que NO es una estructura ordenada por lo que no podremos
    coger un valor por el índice en el que creemos que está."""

other_set = {3,13,23}

print(type(other_set))

other_set.add(33)

print(other_set)

""" Al añadir varias veces el mismo elemento lo único que puede cambiar es su orden
    ya que el set no puede repetir el valor.
    
    Aunque, como en este caso, puede que no cambie de orden"""
other_set.add(33)
print(other_set)

# Podemos realizar búsquedas para ver si está el valor o no en el set

print(5 in other_set)
print(23 in other_set)

# Podemos vaciar el set con clear directamente
my_set = {'a','b','c','d','e'}

print(my_set)

my_set.clear()
print(my_set)

# Hay muchas operaciones similares en set junto a las de list

# Podemos volver a cambiar el tipo por el tipado dinámico de Python

my_set = list()
print(type(my_set))

my_set = set()
my_set = {"Java", "Javascript", "Python"}
print(my_set, type(my_set))

# Operaciones que podemos hacer con set

# Como podemos ver se unen los dos sets sin ningún tipo de orden
union_set = my_set.union(other_set)
print(union_set)

# Por mucho que sigamos haciendo unions no se van añadir más valores porque es un set
union_set.union(other_set).union(my_set)
print(union_set)

# Pero podemos añadirle más valores al set directamente sin tener que crear una variable nueva

print(union_set.union({"HTML", "CSS"}))
# También podemos ver que si pasamos el union sin modificar la variable no la almacena en la variable del set
print(union_set)
print(union_set.difference(other_set))
