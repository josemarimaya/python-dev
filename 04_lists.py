### LISTAS ###

ls = [] # Forma clásica de invocar una lista vacía 
my_list = list() # Lista vacía inicializada por función, ambas opciones son igual de válidas

# Podemos usar las funciones que tiene propiamente el sistema como anteriormente lo hemos hecho

print(len(ls)) 

my_list = [27, 30, 15, 3, 5, 15, 27]

print(my_list)

ls = [27, 1.77, "Josemari", "Maya"]

""" Podemos acceder a los valores de una lista de la misma manera
    que lo hicimos con los strings"""
print(ls[0]) # Acceso a los valores
print(ls[-2]) # Devolveremos el valor en la posición (len(ls) - 2)
# print(ls[-5]) # Evidentemente no podemos acceder a las posiciones que no existen en la lista IndexError

