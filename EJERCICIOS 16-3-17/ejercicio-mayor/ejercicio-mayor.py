#!/bin/python
# coding: utf8

import os

os.system('clear')

num1=input("Escriba un numero: ")
num2=input("Escriba otro numero: ")

if (num1 > num2):
	os.system('clear')
	print "El numero mas grande es: ", num1
elif (num1 == num2):
	os.system('clear')
	print "Els dos valors son iguals!"
else:
	os.system('clear')
	print "El numero mas grande es: ", num2 
