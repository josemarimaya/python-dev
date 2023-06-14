## CONDICIONALES ##

# Básicamente será muy similar a lo que podemos ver en cualquier lenguaje

condition = True

# Evidentemente la estructura del if es distinta a la de Java

if condition:
    print("La condición es " + condition.__str__()) # pequeña transformación de booleano a string

num = 50

if num == 50:
    print("A TOPEEEEEEEEEE")
elif num < 50: # llamada de else if
    print("no tan a tope")
else:
    print("MOAAAAAAAAAAAAAAAAAAAAR A TOPEEEEEEE")

# Los operadores logicos se escriber "directamente"

nota = 2

if nota < 5 or nota == 4:
    print("Estas suspenso macho")

animo = "A TOPISIMO"

if num == 50 and animo.__eq__("A TOPISIMO"): # uso del equals con el string
    print("BUAAAAAAAAAAAAAAAAAMOS")
    num = num - 2

if not(num == 50 and animo.__eq__("A TOPISIMO")):
    print("Macho ya estás bien no")