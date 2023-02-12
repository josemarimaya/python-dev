### STRINGS ###

string_a = "Soy un String"
string_b = 'También soy un String'

print(len(string_a))
print(len(string_b))

print(string_a + " y " + string_b)

# Distintos operadores con string

salto_linea = "Aquí tenemos un \n salto de linea"
tabulacion = "Y aquí tenemos \t una tabulación"

print(salto_linea)
print(tabulacion)


# Formateo de strings

name, surname, age = "Josemari", "Maya", 27

""" Con el formateo lo que hacemos es coger las primeras variables 
    que encuentra nuestro programa para pasarle el tipo de valor que invocas
    Para llamar a un string %s y para llamar a un integer %d
    
    Tienen que relacionarse el tipo del valor de la variable 
    porque sino no se leerá correctamente"""

print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))

""" Para formatearlo con format donde viene el formateo de la variable
    pondremos {}"""

print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))

""" La más óptima es usando el formateo con print(f( {var0} ... {varn}))"""

print(f"Mi nombre es {name} {surname} y mi edad es {age}")


# Desempaquetado de caracteres

""" Relacionamos cada variable a un caracter de la 
    variable que hemos creado y operamos con esa relación"""
languaje = "Python"
a,b,c,d,e,f = languaje
print(f)

# División de strings

print(languaje[1:3])    # Coge los caracteres de rango [i,j). En este caso [1,3) 
print(languaje[2:])     # Coge los caracteres de rango [i]. En este caso [1,3)
print(languaje[-2])     # Coge los caracteres de rango [len - i]. En este caso [len - 2]
print(languaje[::-1])   # Pongo el string al revés


# Funciones varias

print(languaje.capitalize()) # El valor de la variables
print(languaje.upper())      # Nos devuelve el string en mayusculas
print(languaje.lower())      # Nos devuelve el string en minusculas
print(languaje.count("y"))   # Cuenta cuantas veces se repite el valor
print(languaje.upper().isupper()) # Nos devuelve true/false dependiendo si es o no lo que queremos comprobar