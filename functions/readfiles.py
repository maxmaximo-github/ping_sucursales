#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is reboot IPv4 phones.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.5.2"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguezpadilla@gmail.com"
__status__ = "Development"


from glob import glob
from os import getcwd


def read_files():
    """
    Funcion para leer los archivos de los telefonos que estan activos.

    Esta funcion lee los archivos que se encuentran en la carpeta tmp de
    los dispositivos que tuvieron exito a la hora de realizar la prueba de
    ping.
    """
    directory = getcwd()
    devices_alive = []
    for file_name in glob(f"{directory}/tmp/*"):
        with open(file=file_name, mode="r") as f:
            for line in f.readlines():
                devices_alive.append(line)

    return devices_alive
