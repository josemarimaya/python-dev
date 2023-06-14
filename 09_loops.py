## BUCLES/CICLOS/LOOPS ##

""" Recordamos que las estructuras básicas conceptualmente se mantienen
    aunque cambien en forma a la de hora de escribirlas"""

## WHILE ##

count = 0

while count < 10:
    print("Illo esta es la vez " + count.__str__() + " que me repites cabesa")
    count += 1  # count = count + 1

print("Ya hemos salido del primer while")

# Podemos añadirle un else al while, cosa que es única en python

while count is not 0: # El operador is es como == por ende is not es !=
    print("Vamo pa' tra: " + count.__str__())
    if count is 1:
        print("Que ya queda NAAAAAAAAAA")
        # break # Rompemos el bucle
    count -= 1
else:
    print("Ya hemos llegado al principio")


## FOR ##

my_list = [27, 30, 15, 3, 5, 15, 27, 5, 15, 5]

