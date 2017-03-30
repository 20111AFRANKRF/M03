#!/bin/python
# coding: utf8
"""
SWAP. Intercambio de variables
mano_der=”movil”
mano_izq=”bocadillo”
Pista: Usar una variable temporal “mano_extra”
"""
import os

os.system('clear')

print "Primero definiremos la variable"

os.system('sleep 5') 
os.system('clear')

md = "movil"
mi = "bocadillo"
me = ""

print "empezamos con el movil en la mano derecha y el bocadillo en la izquierda"

os.system('sleep 5') 
os.system('clear')
 
me = md

print "copiamos el movil en nuestra 'mano temporal'"

os.system('sleep 5') 
os.system('clear')

md = mi

print "sobreescribimos el movil copiando el bocadillo de la mano izquierda a la derecha"

os.system('sleep 5') 
os.system('clear')

mi = me

print "sobreescribimos el bocadillo de la mano izquierda con el movil copiado en nuestra 'mano temporal'"
