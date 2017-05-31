#!/bin/python
# coding: utf-8
import os
import stat

path_to_explore="./test/"

#Fem una busqueda a tota la estructura dins de /test

for root, dirs, files in os.walk(path_to_explore):

    for name in files:

        name_path=os.path.join(root, name)
        print(name_path)
# Una vegada tenim la ruta del arxius mirem els permisos

        UGOfiles = oct(stat.S_IMODE ( os.stat (name_path).st_mode ))
# Si others (-1) es diferent de 0 significa que te permisos
        if (UGOfiles [-1] != 0):
            print UGOfiles

# Ara farem lo mateix amb els directoris
    for name in dirs:

        name_path=os.path.join(root, name)
        print(name_path)

        UGOdir = oct(stat.S_IMODE ( os.stat (name_path).st_mode ))

        if (UGOdir[-1] != 0):
            print UGOdir
