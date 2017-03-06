# !/usr/bin/python
# -*-coding: utf-8-*-
"""
Lee un número del teclado
Si es:
-par
-entre -10 y 40
-negativo
"""
numero=input("escribe un numero: ")
if numero % 2 == 0 :
	print "Has escrito un numero par"
if numero >= -10 and numero <= 40 :
	print "tu numero esta entre -10 y 40"
if numero < 0 :
	print "tu numero es negativo"
