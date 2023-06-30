## MANEJO DE FICHEROS ##

import os  # Paquete que nos permite el manejo de ficheros

txt_file = open("ficheros/pruebita.txt", "r+")  # El segundo parámetro son los permisos que le damos al fichero

# print(txt_file.read()) # solo podemos leer lo mismo una vez al mismo tiempo

for line in txt_file.readlines():  # readlines() invoca a todas las lineas y las imprimimos una a una
    print(line)

txt_file.write("\nTambién soy un sucio otaku")  # podemos escribir en el propio fichero

print(txt_file.readline())

txt_file.close()

# Para borrar datos del fichero

# os.remove("ficheros/pruebita.txt")


# Manejo de json

import json

# La estructura de json es parecida a la de los diccionarios

json_pruebita = open("ficheros/pruebita_js.json", "w+")  # Podemos crear directamente el fichero si no existe

testito = {"Nombre": "Josemari",
           "Apellido": "Maya",
           "Edad": 27,
           "Estatura": 1.75,
           "Backend": ["Python", "Java"],
           "Frontend": ["Vue", "CSS"]}

# Primero vienen el json que vamos a almacenar y luego dónde lo vamos a almacenar

json.dump(testito, json_pruebita) # Escribimos el json que hemos guardado como variable en el fichero json creado
