
'''
Por convenio no se usa camel case sino snake case

Snake case es escribir_las_variables con _ si tienen alguna separación y con todo en minúsculas

'''
my_variable = "Mi primera variable"
print(my_variable)

my_int_variable = 5

my_bool_variable = True

# Con str transformamos el valor numérico en string

int_to_str = str(my_int_variable)

print(type(int_to_str))

# len nos sirve para saber la longitud de la variable

print(len(my_variable))

# Podemos crear variables en una sola línea

name, surname, alias, age = "José María", "Maya Cano", "Josemari", 27

# No es muy buena práctica ya que si hay mucha distinción de valores nos podemos equivocar al relacionarlos 

print("Soy", name, surname, ", pero me suelen llamar", alias, ". Y tengo", age)

# El espaciado al hacer print lo hace python directamente

#
name = input("¿Cuál es tu nombre?")
age = input("¿Qué edad tienes?")

print("Los datos de la persona usando estos son",name, age, "anyos")
