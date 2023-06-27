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

problem_0 = [i for i in range(1, 100)]

print(problem_0)


def fizz_buzz(problem):
    for i in problem:
        if i % 3:
            problem[i] = "fizz"
        elif i % 5:
            problem[i] = "buzz"
        elif i % 3 and i % 5:
            problem[i] = "fizzbuzz"

    print(problem)


fizz_buzz(problem_0)
