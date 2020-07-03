#!/usr/bin/env  python3
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020, Reboot IPv4 Phones"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.0.2"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguez@gmail.com"
__status__ = "Develop"


import os


def sucursales():
    directory = os.getcwd()
    sucursales_list = []
    for line in open(file=f"{directory}/sucursales/sucursales.txt", mode="r"):
        data_info_list = line.strip("\n").split(", ")

        dictionary = dict()
        dictionary["Sucursal"] = data_info_list[0]
        dictionary["Prefijo"] = data_info_list[1]

        sucursales_list.append(dictionary)

    return sucursales_list
