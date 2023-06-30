## FUNCIONES DE ORDEN SUPERIOR ##

# El resumen es que podemos hacer llamadas a funciones dentro de otras pasandolas como parametros

def operation(value):
    return value * value


def moooore_operations(value, function):
    return function(value * 3)


value_f = 5

# La funcion a la que se le llama dentro de otra no hay que pasarle un parametro ya que la llamas dentro de la principal
print(moooore_operations(value_f, operation))


## CLOSURES ##

def closure_sum(value):
    def add(other_value):
        return value + other_value

    return add


# Podemos guardar la función dentro de una variable siendo esta la más interna

var = closure_sum(5)

# Teniendo que llamar a la variable que almacena la interior con el valor que vas aplicar de manera subsiguiente
print(var(1))

# El concepto se ve mejor de la siguiente manera:

# En el cual podemos ver que primero se coge el principal y luego el subsiguiente

print(closure_sum(5)(4))


def do_things(value):
    def printea(something):
        print(something)

    def resta(other_value):
        return printea(value - other_value)

    return resta


do_things(5)(4)

## Built-in Higher Order Functions

numbers = [7, 56, 648, 9]


# MAP #

def funfunction(number):
    print(number)

# El map lo que nos sirve es a iterar la lista de numbers y pasarle cada valor iterable a la funcion que pasamos

map(funfunction, numbers)

""" Además, podemos provocar que los resultados de usar un map se metan en una lista
    También podemos usar lambds dentro del propio map"""

print(list(map(lambda number: number * 2, numbers)))



# FILTER #

"""Parecido al filter usado en java funcional, usamos un valor iterable para aplicar los datos
   Los cuales se pueden almacenar en una varibale lista o usarlo unicamente para printear
   En vez de definir una función auxiliar se pueden usar lambdas para ello"""

# Hemos hecho un lambda que filter únicamente valores pares

filtration = list(filter(lambda number: number % 2 == 0, numbers))

print(filtration)


## REDUCE ##

# Hay que importarla

from functools import reduce

numbers_again = [3,98,74,6,2]

print(reduce(lambda number1, number2: number1 + number2, numbers_again))



