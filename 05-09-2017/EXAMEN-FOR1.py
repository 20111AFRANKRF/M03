def my_range (inici, fi, augment):
    while inici <= fi:
       yield inici
       inici = inici + augment

for filas in my_range (1,5,1):
       for columnas in my_range (1,4,1):
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
