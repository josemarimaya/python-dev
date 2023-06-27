## LAMBDAS ##

# En resumidas cuentas es una función que se puede almacenar en una variable

sum_values = lambda first, second: first + second

print(sum_values(6, 4))


# Se pueden usar lambdas dentro de otras funciones

def multi(number1, number2):
    return sum_values(number1, number2) * number1


print(multi(5, 5))
