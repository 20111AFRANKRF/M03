# coding:utf-8
# Definimos la funcion my_range

def my_range(inici, fi, increment):
	while inici <= fi:
		yield inici
		inici = inici + increment

# For que nos hace 6 filas
for fil in my_range (1,6,1):
# Este for nos hace 5 columnas
	for col in my_range (1,5,1):
# Condicionamos para que aparezca algun caracter segun la posicion y quede un dibujo de arbol de navidad
			if (fil==4):
				print "A",
			elif ((fil==3) and ((col==2) or (col==3) or (col==4))):
				print "A",
			elif (fil==2 and col==3):
				print "A",
			elif (fil==1 and col==3):
				print "*",
            elif ((fil==6 and col==3) or (fil==5 and col==3)):
                print "N",
            else:
                print "-"
print ""
