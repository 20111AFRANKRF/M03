#!/bin/python
# -*-coding: utf-8-*-
"""
Menu de una calculadora:
Qué desea hacer el amo?
1.- Sumar
2.- Restar
3.- Multiplicar
4.- Dividir
5.- Salir

Nota: si el usuario elige un número que no está entre 1 y 5->Error “Esa opción no existe”
"""
import os

sortir=False

while sortir==False:  
	
	print "1.- Sumar"
	print "2.- Restar"
	print "3.- Multiplicar"
	print "4.- Dividir"
	print "5.- Salir"

	numero=input("Que desea hacer el amo?: ")
	
	if numero == 1:
		print "Introduce dos numeros:"
		x=input("numero 1: ")
		y=input("numero 2: ")

		print "El resultado de la suma es: ", x+y
		
		tecla=raw_input("Presiona una tecla para continuar...")
		
		os.system('clear')

	elif numero == 2:
		x=input("numero 1: ")
		y=input("numero 2: ")

		print "La resta es: ", x-y
		
		tecla=raw_input("Presiona una tecla para continuar...")
		
		os.system('clear')

	elif numero == 3:
		x=input("numero 1: ")
		y=input("numero 2: ")

		print "La multiplicació es: ", x*y
		
		tecla=raw_input("Presiona una tecla para continuar...")

		os.system('clear')

	elif numero == 4:
		x=input("numero 1: ")
		y=input("numero 2: ")

		print "La divisió es: ", x/y

		tecla=raw_input("Presiona una tecla para continuar...")

		os.system('clear')
		
	elif numero == 5:
		print "ADIOS!"
		sortir=True
	else:
		print "ERROR! La opció no existeix"
		tecla=raw_input("Presiona una tecla para volver al menu...")
		os.system('clear')
