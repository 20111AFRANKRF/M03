def my_range(inici, fi, increment):
	while inici <= fi:
		yield inici
		inici = inici + increment

for filas in my_range (1,8,1):
    for columnas in my_range (1,8,1):
        if (filas % 2 <> 0) and (columnas % 2 <> 0):
            print "-", 
        elif (filas % 2 <> 0) and (columnas % 2 <> 0):
            print "-",
print " "
