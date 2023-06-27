## MODULOS ##

# Importamos nuestro fichero local

import module
import math # libreria propia del sistema

module.resta(7,5) # La llamada se hace parecido a un objeto

# Para obtener únicamente una función

# from module import suma

# Y podríamos usarlas directamente

# suma(8,9)


import random

ciudades = ["Sevilla", "Cadiz", "Malaga", "Huelva", "Almeria", "Jaen", "Cordoba"]

ciudad_random = random.choice(ciudades)

print(ciudad_random)