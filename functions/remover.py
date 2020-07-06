#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is create for general propouse.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020, Reboot IPv4 Phones"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.0.2"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguez@gmail.com"
__status__ = "Develop"


import os
import glob
from os import remove


def remover_files():
    """
    Funcion para eliminar archivos de la carpeta tmp.

    Esta funcion elimina los archivos que se crean al realizar las acciones
    por las diferentes fuciones que crean archivos y los guardan temporalmente
    para su tratamiento posterior evitando asi que en ejecucion de hilos
    posteriores estos sean leidos y realizado las acciones pertienentes.
    """
    directory = os.getcwd()
    for file_name in glob.glob(("{}/tmp/*").format(directory)):
        remove(file_name)
