#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
import os

os.system('clear')

jugador1=raw_input("Possi la jugada (PE/PA/TI/LA/SP):")

aleatori=randint(1,5)
if (aleatori==1):
	jugador2="PE"
if (aleatori==2):
	jugador2="PA"
if (aleatori==3):
	jugador2="TI"
if (aleatori==4):
	jugador2="LA"
if (aleatori==5):
	jugador2="SP"


if (jugador1==jugador2):
	os.system('clear')
	print "Has seleccionado ", jugador1
	print "La maquina ha sacado: ", jugador2
	print "Empat"
else: 
	if ( (jugador1=="PE" and (jugador2=="LA" or (jugador2=="TI"))) or
	     (jugador1=="PA" and (jugador2=="PE" or (jugador2=="SP"))) or
	     (jugador1=="TI" and (jugador2=="PA" or (jugador2=="LA"))) or
		 (jugador1=="LA" and (jugador2=="PA" or (jugador2=="SP"))) or
		 (jugador1=="SP" and (jugador2=="PE" or (jugador2=="TI"))) 
	    ):
		os.system('clear')
		print "Has seleccionado ", jugador1
		print "La maquina ha sacado: ", jugador2
		print "Tu guanyes!!!!!"
	else:
		os.system('clear')
		print "Has seleccionado ", jugador1
		print "La maquina ha sacado: ", jugador2
		print "Ets un .... has perdut !!!!"
