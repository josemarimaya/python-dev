## BUCLES/CICLOS/LOOPS ##

""" Recordamos que las estructuras básicas conceptualmente se mantienen
    aunque cambien en forma a la de hora de escribirlas"""

## WHILE ##

count = 0

while count < 10:
    print("Illo esta es la vez " + count.__str__() + " que me repites cabesa")
    count += 1  # count = count + 1

print("Ya hemos salido del primer while")

# Podemos añadirle un else al while, cosa que es única en python

while count != 0: # El operador is es como == por ende is not es !=
    print("Vamo pa' tra: " + count.__str__())
    if count == 1:
        print("Que ya queda NAAAAAAAAAA")
        # break # Rompemos el bucle
    count -= 1
else:
    print("Ya hemos llegado al principio")


## FOR ##

my_list = [27, 30, 15, 3, 5, 15, 27, 5, 15, 5]

for element in my_list: # element va a ser el elemento que se itera en cada bucle, como i en for(int i= ...)
    print(element) # los element en los for son el nombre de una variable local para cada for

my_set = {"Java", "Javascript", "Python"}

for element in my_set:
    print(element)

my_tuple = (27, 1.75, "Josemari", "Maya")

for element in my_tuple:
    print(element)

my_dict = {"Nombre": "Josemari",
              "Apellido": "Maya",
              "Edad": 27,
              "Estatura": 1.75,
              "Backend": {"Python", "Java"},
              "Frontend": {"Vue", "CSS"}}

for element in my_dict: # en los diccionarios lo que itera es sobre las claves, no sobre los values
    print(element)
    if element == "Apellido":
        print(element)
        break
else: # al hacer un break no se puede usar el else al finalizar el for
    print("Ejecucion terminada")