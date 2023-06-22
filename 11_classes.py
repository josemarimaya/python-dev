## CLASES ##

# Para definir las clases lo único que necesitamos en la palabra reservada class

class EmptyPerson:  # definimos las clases en CamelCase
    pass  # para que no de error si no hay nada


class Person:
    # se usa self para definir la propia clase y pueda recibir parametros
    def __init__(self, name, surname, alias = "Sin alias"):  # el valor por defecto del atributo alias va a ser Sin alias
        """ Tenemos que hacer la llamada a self para definir el name y surname de esa clase.
            De manera similar a como se puede hacer en Java con la asignación de atributos.

            Es obligatorio, ya que sino de esta manera, name y surname no se quedan como atributos de la clase"""

        self.name = name
        self.surname = surname
        self.alias = alias

    def walking(self):  # usamos siempre self para la llamada a los atributos de la clase
        nombre_completo = self.name + " " + self.surname
        print("Chavalito " + nombre_completo + " está caminando")


myself = Person("Josemari", "Maya")
print(myself)

myself.walking()

print(myself.alias)
# Podemos modificar atributos de la clase directamente fuera de la misma
myself.alias = "SirMalvado"
print(myself.alias)


