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


from functions.cleanscreen import clean_screen


color_reset = "\x1b[0m"
red = "\x1b[00;00;1;031m"
red_blink = "\x1b[00;00;5;031m"
magent = "\x1b[00;00;02;033m"
magent_blink = "\x1b[00;00;02;033m"
blue = "\x1b[00;00;1;034m"
blue_blink = "\x1b[00;00;5;034m"
green = "\x1b[00;00;01;092m"
green_blink = "\x1b[00;00;5;092m"


def dictionary_prefix(creacion_prefijos, sucursales_list):
    """
    Funcion para crear los dictionarios.

    Esta funcion crea los indices necesario para el manejo de las sucursales
    a traves del menu.
    """
    try:
        dictionary_prefijos = []
        for prefijo in creacion_prefijos:

            dict_sucursal = sucursales_list[prefijo]
            tmp_prefijo = dict_sucursal["Prefijo"]
            tmp_prefijo = tmp_prefijo.split(".")
            tmp_prefijo = ".".join(tmp_prefijo[0:3])

            name_sucursal = dict_sucursal["Sucursal"]

            dictionary_list = {}
            tmp_ip_list = []
            for ip in range(1, 255):
                tmp_ip_list.append(f"{tmp_prefijo}.{ip}")

            dictionary_list[name_sucursal] = tmp_ip_list
            dictionary_prefijos.append(dictionary_list)

    except IndexError:
        clean_screen()

        sucursales_inexistentes = []
        for no_sucursal in creacion_prefijos:
            if no_sucursal > len(sucursales_list)-1:
                sucursales_inexistentes.append(no_sucursal)

        print(f" {green}{'='*66}")
        print(f" {blue_blink} {('Precaucion '*6):^40}")
        print(f" {green}{'='*66}")
        print(
            f" {red}El programa {green}NO REALIZARA ACTIVIDAD"
            + f" {red}en las siguientes sucursales")
        print(f" {red}debido a lo siguiente:{color_reset} \n")
        print(f" {red}Las siguientes sucursales no existen: ")
        print(f"\t\t{green}{sucursales_inexistentes}{color_reset}\n")

    return dictionary_prefijos
