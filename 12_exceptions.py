## MANEJO DE ERRORES ##

""" Las palabras reservadas para manejar los errores son:

    - try: ejecutar el codigo directamente si funciona
    - catch: ejecutar el codigo aunque tenga errores
    - else: ejecutar el codigo si no tiene excepciones
    - finally: ejecutar siempre el codigo"""


def resta(number, other_number):
    rs = number - other_number
    print(rs)


numberOne = 1
numberTwo = 7

# Probamos el codigo del error
try:
    numberTwo = "Aaaaaay buenas tardessss"
    resta(numberOne, numberTwo)
    print("Sin errores")
except:
    print("No has metido dos numeros, hemos probado el error")
else:
    print("La ejecución se ha ejecutado correctamente")


# Probamos sin erores
try:
    numberTwo = 10
    resta(numberOne, numberTwo)
    print("Sin errores")
except:
    print("No has metido dos numeros")
else: # cuando funciona bien se sigue ejecutando, es opcional
    print("La ejecución se ha ejecutado correctamente")
finally: # OPCIONAL
    print("Ejecucion correcta terminada")


# Probamos el codigo del error con tipos
try:
    numberTwo = "Aaaaaay buenas tardessss"
    resta(numberOne, numberTwo)
    print("Sin errores")
except TypeError: # Podemos añadirle excepciones por las diferentes excepciones
    print("Ha fallado por el tipo de valor")
except ValueError:
    print("Error en los valores")


# Probamos el codigo almacenando el error en variable
try:
    numberTwo = "Aaaaaay buenas tardessss"
    resta(numberOne, numberTwo)
    print("Sin errores")
except TypeError as error: # almacenamos el tipo de error en una variable
    print(error)
except Exception as generic_error: # Exception es para excepciones genéricas
    print(generic_error)
