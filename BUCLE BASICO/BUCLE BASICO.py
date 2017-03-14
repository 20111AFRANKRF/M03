#!/bin/python
# -*-coding: utf-8-*-

"""
Hacer un bucle que lea una opción del usuario del 1 al 5.
Imprime “La opción seleccionada es: 2”
Cuando sea 5 sale del bucle.
"""
import os
os.system('clear')

print "opcio 1"
print "opcio 2"
print "opcio 3"
print "opcio 4"
print "salir"

numero=input("seleccione una opcion: ")

os.system('clear')

while (numero >0 and numero <= 4):
	if numero == 1:
		print "La opcion seleccionada es 1"
		numero=input("seleccione una opcion: ")
		
		os.system('clear')

	elif numero == 2:
		print "La opcion seleccionada es 2"
		numero=input("seleccione una opcion: ")

		os.system('clear')

	elif numero == 3:
		print "La opcion seleccionada es 3"
		numero=input("seleccione una opcion: ")

		os.system('clear')

	elif numero == 4:
		print "La opcion seleccionada es 4"
		numero=input("seleccione una opcion: ")

		os.system('clear')


