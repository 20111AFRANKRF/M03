# coding: utf-8
# Definimos la funcion my_range
def my_range(inici, fi, increment):
	while inici <= fi:
		yield inici
		inici = inici + increment
# Creamos un for que nos hace 8 filas
for filas in my_range (1,8,1):
# Y otro for que nos hace 8 columnas
	for columnas in my_range (1,8,1):
# Condicionamos segun sean pares o impares por la posicion 
        if (filas % 2 <> 0) and (columnas % 2 <> 0):
            print "-",
        elif (filas % 2 <> 0) and (columnas % 2 <> 0):
            print "-",
print " "
