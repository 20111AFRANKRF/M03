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

print "***CALCULADORA***"
os.system('clear')

print "1.- Sumar"
print "2.- Restar"
print "3.- Multiplicar"
print "4.- Dividir"
print "5.- Salir"

numero=input("Que desea hacer el amo?: ")

os.system('clear')

if numero == 1:
	print "Introduce dos numeros:"
	x=input("numero 1: ")
	y=input("numero 2: ")
	print "La suma es: ", x+y
elif numero == 2:
	x=input("numero 1: ")
	y=input("numero 2: ")
	print "La resta es: ", x-y
elif numero == 3:
	x=input("numero 1: ")
	y=input("numero 2: ")
	print "La multiplicació es: ", x*y
elif numero == 4:
	x=input("numero 1: ")
	y=input("numero 2: ")
	print "La divisió es: ", x/y
elif numero ==5:
    print "ADIOS!"

