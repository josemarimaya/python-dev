## FUNCIONES DE ORDEN SUPERIOR ##

# El resumen es que podemos hacer llamadas a funciones dentro de otras pasandolas como parametros

def operation(value):
    return value * value


def moooore_operations(value, function):
    return function(value * 3)


value_f = 5

# La funcion a la que se le llama dentro de otra no hay que pasarle un parametro ya que la llamas dentro de la principal
print(moooore_operations(value_f, operation))


## Closures ##

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

numbers = [1,56,648,9]

# Map

map()

