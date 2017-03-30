#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os 

os.system('clear')

print "PIEDRA-PAPEL-TIJERAS"
print "--reglas-- Debes escoger una entre estas tres opciones:"
print "1. PIEDRA"
print "2. PAPEL"
print "3. TIJERA"
print "El ganador sera decidido despues de que los dos ganadores hayan echo su eleccion..."
print "P.D: La eleccion tiene que ser en mayusculas"

J1=raw_input("Seleccione Opcion: ")
J2=raw_input("Seleccione Opcion: ")
salir=False
while (salir==False):
	if (J1 == "PIEDRA" and J2 == "PAPEL"):
		J2="WIN"
		print "J2 WIN"
	if (J1 == "PIEDRA" and J2 == "TIJERA"):
		J1="WIN"
		print "J1 WIN"
	if (J1 == "PIEDRA" and J2 == "PIEDRA"):
		J1="NWIN"
		J2="NWIN"
		print "EMPATE - NO HAY GANADOR"
	if (J1 == "PAPEL" and J2 == "PIEDRA"):
		J1="WIN"
		print "J1 WIN"
	if (J1 == "PAPEL" and J2 == "TIJERA"): 
		J2="FIN"
		print "J2 WIN"
	if (J1 == "PAPEL" and J2 == "PAPEL"):
		J1="NWIN"
		J2="NWIN"
		print "EMPATE - NO HAY GANADOR"
	if (J1 == "TIJERA" and J2 == "PIEDRA"):
		J2="WIN"
		print "J2 WIN"
	if (J1 == "TIJERA" and J2 == "PAPEL"):
		J1="WIN"
		print "J1 WIN"
	if (J1 == "TIJERA" and J2 == "TIJERA"):
		J1="NWIN"
		J2="NWIN"
		print "EMPATE - NO HAY GANADOR"
	if (J1 == "WIN") or (J2 == "WIN") or (J1 == "NWIN" and J2 == "NWIN"): 
		salir=True
