#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
aleat1=randint(1,4)
aleat2=randint(1,4)
j1=randint(1,13)
j2=randint(1,13)
salir=False
while (salir==false):
	if (aleat1==1):
		aleat1="picas"
	if (aleat1==2):
		aleat1="treboles"
	if (aleat1==3):
		aleat1="diamantes"
	if (aleat1==4):
		aleat1="corazones"
	if (aleat2==1):
		aleat2="picas"
	if (aleat2==2):
		aleat2="treboles"
	if (aleat2==3):
		aleat2="diamantes"
	if (aleat2==4):
		aleat2="corazones"
	if (j1==j2):
		print "Empate"
	elif (j1 > j2):
		if (j1==11):
			j1="J"
		if (j1==12):
			j1="Q"
		if (j1==13):
			j1="K"
		print "j1 saca", j1, "de", aleat1
		print "j2 saca", j2, "de", aleat2
		print "j1 gana"
		
	elif (j2==11):
		j2="J"
	if (j2==12):
		j2="Q"
	if (j2==13):
		j2="K"
	print "j1 saca", j1, "de", aleat1
	print "j2 saca", j2, "de", aleat2
	print "j2 gana"
		
