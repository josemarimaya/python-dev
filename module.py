## FICHERO AUXILIAR ##

def resta(number, other_number):
    rs = number - other_number
    print(rs)


def suma(number, other_number):
    rs = number + other_number
    print(rs)


def genera_permutacion_inversa(lista_ciudades):
    numero_ciudades = len(lista_ciudades)

    ciudad_1 = random.choice(range(0, numero_ciudades))
    print(lista_ciudades[ciudad_1])
    ciudad_2 = random.choice(range(0, numero_ciudades))
    print(lista_ciudades[ciudad_2])
    nueva_lista = lista_ciudades[ciudad_1::-1] + lista_ciudades[ciudad_2::-1]

    ciudades_set = set(nueva_lista)
    return nueva_lista, ciudades_set
