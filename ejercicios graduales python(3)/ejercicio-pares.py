# !/usr/bin/python
# -*-coding: utf-8-*-
"""
Lee un número del teclado
Si es par: Escribe “Qué bonito número par”
Si es impar: Escribe “Qué número más vulgar”
Pista: usar módulo %
"""
numero=input("escribe un numero: ")
if numero % 2 == 0 :
	print 'Que bonito numero par'
if numero % 2 != 0 :
	print 'Que numero mas vulgar' 
