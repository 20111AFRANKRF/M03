def my_range(inici, fi, increment):
	while inici <= fi:
		yield inici
		inici = inici + increment

for filas in my_range (1,4,1):
	for columnas in my_range (1,8,1):
		if (columnas==1 or columnas==8):
			print "*",
		else:
			if (filas==1 or filas==4):
				print "*",
			else:
				print "-",
print ""
