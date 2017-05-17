 # coding: utf-8
import calendar

def my_range(inici,fi,increment):
    while inici <= fi:
        yield inici
        inici = inici + increment
# Informacion que queremos mostrar
info=input("De quin mes vols veure el calendari?")
info2=input("De quin any vols veure el calendari?")
# monthrange nos dira el dia que de la semana que comienza el mes y los dias que tiene
diasMes=calendar.monthrange(info2, info)
# Definimos las variables
espacios=diasMes[0]
primero=diasMes[0]+1
ultimo=diasMes[1]
numDia=1
# Mostramos la cabecera, para monthrange el Lunes empieza con el 0 por eso sumamos 1 en la variable
print "L M X J V S D"
# Bucle para la estructura del calendario
for filas in my_range(1, 6, 1):
    for columnas in my_range(1,7,1):
# Bucle para los espacios
        for columnas in my_range(1, espacios, 1):
            print " ",
# Bucle para los dias
        for columnas in my_range(primero, 7, 1):
            if (numDia <= ultimo):
                print numDia,
                numDia=numDia+1
            else:
                print " "
# Print para el salto de linia al terminar la columna
        print ""
