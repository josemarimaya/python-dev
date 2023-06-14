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

# Para coger las distintas propiedades del diccionario tenemos lo siguiente

# Los items del diccionario
print(other_dict.items())
# Las keys del diccionario
print(other_dict.keys())
# Los values del diccionario
print(other_dict.values())

# Así podremos acceder directamente a ver si los valores están en el diccionario

print("Maya" in other_dict.values())

# Podemos crear un diccionario con claves directamente usando...

# ... si nos olvidamos del doble paréntesis no meterá bien las keys

pict = dict.fromkeys(("Nombre", "Apodo"))
print(pict)

# La mejor utilidad es crear un diccionario vacío con las claves

other_dict_2 = dict.fromkeys(other_dict)
print(other_dict_2)