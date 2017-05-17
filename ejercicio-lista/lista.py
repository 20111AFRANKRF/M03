 # coding: utf-8
 # Ejercicio con listas haremos que se reparta una baraja y que cada vez que esta se reparta se decartara de la baraja de forma que no volvera asalir
import random

def my_range(inici,fi,increment):
    while inici <= fi:
        yield inici
        inici = inici + increment

corazones=["AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC"]
treboles=["AT", "2T", "3T", "4T", "5T", "6T", "7T", "8T", "9T", "10T", "JT", "QT", "KT"]
diamantes=["AD", "2D", "3D", "4D", "5D", "6D","7D", "8D", "9D", "10D", "JD", "QD", "KD"]
picas=["AP", "2P", "3P", "4P", "5P", "6P", "7P", "8P", "9P", "10P", "JP", "QP", "KP"]
# Primero un bucle para los diferentes tipo de cartas
for tipos in my_range(1, 4, 1):
    if (tipos == 1):
        tipo = corazones
    elif (tipos == 2):
        tipo = treboles
    elif (tipos == 3):
        tipo = diamantes
    else:
        tipo = picas
# Mostramos el estado de la lista
    print tipo
    for cartas in my_range(0, 12, 1):
# Repartimos las cartas
        print tipo[cartas]
# Despues de repartilas las eliminamos de la lista
        tipo.remove(tipo[cartas])
# Mostramos el resultado final de la lista
        print tipo
