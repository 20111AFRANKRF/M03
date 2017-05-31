#  coding: utf-8
# definimos la funcion my_range
def my_range (inici, fi, augment):
    while inici <= fi:
       yield inici
       inici = inici + augment
# for que nos hace 5 filas
for filas in my_range (1,5,1):
    # for que nos hace 4 columnas
       for columnas in my_range (1,4,1):
        #    condicionamos para que aparezca segun la tabla que aqueremos
        #   las comas concatenan con el siguiente print
            if ( filas == 1):
                 if (columnas == 2):
                     print "A",
                 elif (columnas == 3):
                     print "B",
                 elif (columnas == 4):
                     print "C",
                 else:
                     print "-",
            else:
                if (columnas == 1):
                    print filas -1
                else:
                    print "-",
print " "
