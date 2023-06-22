## FUNCIONES ##

# Definimos la función con la palabra reservada def

def my_function():
    print("La mega función")


my_function()


def suma_simple(first_number, second_number):  # definición de los parametros, aunque no definamos su tipo
    suma = first_number + second_number
    print(suma)


suma_simple(2, 5)

my_list = [27, 30, 15, 3, 5, 15, 27, 5, 15, 5]


def sum_for(lista):  # como está debilmente tipado lo único que tenemos que hacer es pasar un nombre de parámetro
    suma = 0
    for element in lista:
        suma = suma + element

    print(suma)


sum_for(my_list)  # tenemos que tener muy claro lo que vamos hacer con los parametros que vamos a usar

my_dict = {"Nombre": "Josemari",
           "Apellido": "Maya",
           "Edad": 27,
           "Estatura": 1.75,
           "Backend": {"Python", "Java"},
           "Frontend": {"Vue", "CSS"}}


def print_name(dictionary):
    complete_name = ""
    for element in dictionary:
        if (element == "Nombre") or (element == "Apellido") and complete_name == "":  # el parámetro está vacío
            complete_name = dictionary[element]
        elif (element == "Nombre") or (element == "Apellido"):
            complete_name = complete_name + " " + dictionary[element]
    print(complete_name)


print_name(my_dict)


# Caso especial de Python, puedo meterle varios parametros del mismo tipo tipando solamente uno con el *

def text(*text):  # funcionaría igual que una lista
    for txt in text:
        print(txt)


text("Buena", "Python", "Bro")

import math


def cuadrada(number):
    raiz = math.sqrt(number)
    print(f"La raiz cuadrada de {number} es: " + raiz.__str__())


cuadrada(9)
