#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is create for ping IPv4.

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


from os import getcwd


def sucursales():
    """
    Funcion para testear IPv4.

    Esta funcion realiza el testeo de Ping.

    Si el resultado es exitoso se guarda en un archivo de texto, de no ser asi
    sino solo se anuncia que no tiene conectividad.
    """
    directory = getcwd()
    sucursales_list = []
    for line in open(file=f"{directory}/sucursales/sucursales.txt", mode="r"):
        data_info_list = line.strip("\n").split(", ")

        dictionary = dict()
        dictionary["Sucursal"] = data_info_list[0]
        dictionary["Prefijo"] = data_info_list[1]

        sucursales_list.append(dictionary)

    return sucursales_list
