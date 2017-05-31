# coding: utf-8
# definimos la funcion my_range
def my_range(inici, fi, increment):
	while inici <= fi:
		yield inici
		inici = inici + increment
# for que nos hace 4 filas
for filas in my_range (1,4,1):
# for que nos hace 8 columnas
	for columnas in my_range (1,8,1):
# condicionamiento segun dibujo examen
		if (columnas==1 or columnas==8):
			print "*",
		else:
			if (filas==1 or filas==4):
				print "*",
			else:
				print "-",
print ""
