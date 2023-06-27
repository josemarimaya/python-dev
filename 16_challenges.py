## RESOLUCION DE DISTINTOS PROBLEMAS ##

## Reto #0: EL FAMOSO "FIZZ BUZZ”

"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 """

problem_0 = [i for i in range(1, 101)]

print(problem_0)


def fizz_buzz(problem):
    for i in problem:
        if i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")


fizz_buzz(problem_0)

# Reto #1: ¿ES UN ANAGRAMA?

"""/*
 Escribe una función que reciba dos palabras (String) y retorne
 verdadero o falso (Bool) según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
 */"""


def es_anagrama(palabra_1, palabra_2):
    res = None

    palabra_1 = palabra_1.lower()
    palabra_2 = palabra_2.lower()
    if palabra_1 == palabra_2:
        return False
    else:
        if len(palabra_1) == len(palabra_2):
            for i in range(len(palabra_1)):
                if palabra_1[i] == palabra_2[len(palabra_1) - (i + 1)]:
                    res = True
                else:
                    res = False

    return res


print(es_anagrama("AmOr", "roma"))

print(es_anagrama("roto", "toro"))

# FIBONACCI

""" /*
  Escribe un programa que imprima los 50 primeros números de la sucesión
  de Fibonacci empezando en 0.
  - La serie Fibonacci se compone por una sucesión de números en
    la que el siguiente siempre es la suma de los dos anteriores.
    0, 1, 1, 2, 3, 5, 8, 13...
 """


def fibonacci():
    ls = []

    for i in range(50):

        if len(ls) < 2:
            ls.append(i)
        else:
            suma = ls[i - 1] + ls[i - 2]
            ls.append(suma)

    return ls


print(fibonacci())

# NUMEROS PRIMOS


"""
 Escribe un programa que se encargue de comprobar si un número es o no primo.
 Hecho esto, imprime los números primos entre 1 y 100.
 """


def es_primo(number):
    res = True
    if number < 2:
        return False

    for index in range(2, number):
        if number % index == 0:
            res = False

    return res


def primos():
    ls = [i for i in range(1, 101)]  # Recordamos que in range usa intervalos abiertos

    res = []
    for i in range(2, 100):  # el 1 es primo
        if es_primo(i):
            res.append(i)

    return res


print(primos())

# INVERSION DE CADENAS

"""
   
 Crea un programa que invierta el orden de una cadena de texto
 sin usar funciones propias del lenguaje que lo hagan de forma automática.
 - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 
 """


def revert(texto):

    reverse_text = ""

    tam = len(texto)

    for i in range(tam):
        # reverse_text[i] = texto[tam - (i + 1)]
        reverse_text += texto[tam - (i + 1)]

    return reverse_text


print(revert("Hola Mundo"))
