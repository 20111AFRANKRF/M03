#!/bin/python
# coding: utf-8
##########################################################################
#                               IMPORTS                                  #
##########################################################################
import os
path_to_explore="./test"

# FAREM QUE AMB EL FOR BUSQUI PER EL DIRECTORI
for root, dirs, files in os.walk(path_to_explore):
# DEMANEM EL PES Y RUTA DELS ARXIUS
    for name in files:

        name_path=os.path.join(root, name)
        print(name_path)
        print os.stat(name_path).st_size
        print os.path.getsize(name_path)

# DEMANEM PERS I RUTA DELS DIRECTORIS
    for name in dirs:

        name_path=os.path.join(root, name)
        print(name_path)
        print os.stat(name_path).st_size
        print os.path.getsize(name_path)
