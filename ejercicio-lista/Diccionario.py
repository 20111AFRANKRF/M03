# coding: utf-8
# HORARIO
materia["Lunes"]=["M01(2H), M05(2H), M09(1H)"]
materia["Martes"]=["M09(1H), M03(2H), M02(2H)"]
materia["Miercoles"]=["M02(2H)", "M01(2H)", "M09(1H)"]
materia["Jueves"]=["M10(1H), M03(2H), M05(1H), M01(2H)"]
materia["Viernes"]=["M10(1H)", "M05(2H)", "HTML(2H)"]

# MENU
sortir=False
while (sortir==False):

    print "        HORARIO EDT       "
    print " 1.- Materias Lunes       "
    print " 2.- Materias Martes      "
    print " 3.- Materias Miercoles   "
    print " 4.- Materias Jueves      "
    print " 5.- Materias Viernes     "
    print " 6.- Salir                "

    seleccion=input("Que materias quieres ver? ")

    if (seleccion == 1):
        print materia["Lunes"]
    elif (seleccion == 2):
        print materia["Martes"]
    elif (seleccion == 3):
        print materia["Miercoles"]
    elif (seleccion == 4):
        print materia["Jueves"]
    elif (seleccion == 5):
        print materia["Viernes"]
    else:
        sortir=True
