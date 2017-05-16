#!/bin/python
# coding:utf-8
##############################################################################
#                                     IMPORTS                                #
##############################################################################
from random import randint
##############################################################################
#                                      NIVEL 2                               #
##############################################################################

# Carta que saca J1
def jugada_j1():
    j1=randint(2,14)
    palo1=randint(1,4)

    numero=j1
    if (j1==11):
        numero="J"
    if (j1==12):
        numero="Q"
    if (j1==13):
        numero="K"
    if (j1==14):
    	numero="A"

    if (palo1==1):
        pal="P"
    if (palo1==2):
        pal="T"
    if (palo1==3):
        pal="D"
    if (palo1==4):
        pal="C"

    print "J1 SACA: " , numero, "de " , pal
#  Carta que saca J2
def jugada_j2():
    j2=randint(1,13)
    palo2=randint(1,4)

    numero2=j2
    if (j2==11):
        numero="J"
    if (j2==12):
        numero="Q"
    if (j2==13):
        numero="K"
    if (j2==14):
    	j2="A"

    if (palo2==1):
        pal2="P"
    if (palo2==2):
        pal2="T"
    if (palo2==3):
        pal2="D"
    if (palo2==4):
        pal2="C"

    print "J2 SACA: " , numero2, "de " , pal2
# Resultados de las jugadas
def resultados():
    if (numero==numero2):
        print "Empat"
    else:
        if (numero>numero2):
            print "GANA J1"
        else:
            print "GANA J2"
################################################################################
#                               NIVEL 1                                        #
################################################################################

# Accionamos que carta sacara J1
def jugada_j1():

# Accionamos que carta sacara J2
def jugada_j2():

#Accionamos los resultados que obtendran segun la carta que hayan sacado
def resultados():
