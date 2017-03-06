# !/usr/bin/python
# -*-coding: utf-8-*-
"""
Lee la edad del teclado
Si tiene 
-entre 18 y 23 años (ambos incluídos) 
-O 17
le decimos que puede entrar en la sesión de jóvenes.
Pista: usar paréntesis ()
"""
edad=input("indica tu edad: ")
if (edad >= 18 and edad <= 23) or edad == 17:
	print "puedes entrar a la sesion de jovenes"
else:
	print "no puedes entrar a la sesion de jovenes"
