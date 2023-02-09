### OPERADORES ###

# Operadores aritméticos básicos

print(3 + 4)
print(3 - 4)
print(3 * 4)
# La operación con una barra si tiene decimales el resultado es un float
print(3 / 4)

# El más "extraño" es el resto
print(8 % 2)
# Usando doble barra aproximamos el resultado de la división a un valor entero
print(10//3)
# Doble asterisco para hacer el exponente
print(3**5)


# Concatenación de strings
print("Buenas"+" Tardes")

""" Como no podemos usar valores de distinto tipo ej: print("Buenas " + 2)
    ahí sí que tendremos convertir el valor para que sean del mismo tipo"""

print("Buenas "+ str(222))

""" Hay una operación que permite usar String con Integer y son aquellas de multiplicación
    que lo que permiten es repetir el mismo String por el valor multiplicativo
    
    Teniendo claro que no se puede hacer la operación con un Float ej: print("Hola "* 50.5)"""

print("Buenas  " * 5)


# Operadores comparativos

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)


""" Cuando tratamos con Strings al comparlos estamos comparando su orden alfabético
    a no ser que le digas forzosamente que comparas por tamaño de texto"""

print("Hola" > "Adios")
print(len("Hola") > len("Adios"))

# Operadores lógicos

""" Pequeño repunte de que al contrario que en la mayoría de los
    lenguajes de programación no se usan los símbolos lógicos sino que 
    por sintaxis se escriben literalmente"""

print(1>2 and 2<3) # and = &&
print(1<2 and "Hola" > "Adios") # or = ||
print(1< 2 or "Hola" > "Adios")
print(not(1<2)) # not = !