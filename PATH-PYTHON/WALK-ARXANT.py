#!/bin/python
# coding: utf-8
##########################################################################
#                               IMPORTS                                  #
##########################################################################
import os
import time
from datetime import datetime, timedelta
# CODI A EXECUTAR
path_to_explore="./test/"

# FAREM QUE AMB EL FOR BUSQUI PER EL DIRECTORI
for root, dirs, files in os.walk(path_to_explore):
# DEMANEM EL PES Y RUTA DELS ARXIUS
    for name in files:
# Amb la funció datetime.now() podem saber la data d'avui
        diaHoy=datetime.now()
# Amb la funcio timedelta seleccionem la cuantitat de dias que vols restar a una data
        dias=timedelta(days=365)
# El resultat de la resta de dates
        Resultado=diaHoy-dias
        name_path=os.path.join(root, name)
        size=os.path.getsize(name_path)

        if (time.ctime(os.path.getctime(str(files)) > Resultado)):
            print files
'''
# DEMANEM PERS I RUTA DELS DIRECTORIS
    for name in dirs:

        diaHoy=datetime.now()
        dias=timedelta(days=365)
        Resultado=diaHoy-dias
        name_path=os.path.join(root, name)
        size=os.path.getsize(name_path)

        if ((time.ctime(os.path.getatime(str(dirs)))) > Resultado) and (size > 1024**3):
            print dirs
'''
