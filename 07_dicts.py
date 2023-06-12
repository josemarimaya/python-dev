## DICCIONARIOS ##

# Los diccionarios ÚNICAMENTE se pueden crear con el constructor dict()

my_dict = dict()

print(type(my_dict))

# Si quisiéramos definirlo lo que tendríamos que hacer es pasarle a mano la forma de un diccionario

other_dict = {"Nombre": "Josemari",
              "Apellido": "Maya",
              "Edad": 27,
              "Estatura": 1.75,
              "Backend": {"Python", "Java"},
              "Frontend": {"Vue", "CSS"}}

""" La definición de diccionario es parecida a la de los HashMaps en Java
    por lo que nos encontramos una estructura clave-valor"""

print(other_dict)

# El tamaño del diccionario viene definido por la cantidad de claves que tiene
print(len(other_dict))

# Accedemos al valor que hay en la clave
print(other_dict["Backend"])

# Podemos añadir o actualizar el dict igualando el dict con la misma relación clave valor
my_dict["Peliculas"] = ["Quantumania", "Spiderverse 2"]

print(my_dict)

my_dict["Peliculas"].insert(2,"Wakanda Forever")

print(my_dict)