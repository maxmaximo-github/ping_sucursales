#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is reboot IPv4 phones.

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
__status__ = "Development"


from functions.cleanscreen import clean_screen
from functions.dictionaryprefix import dictionary_prefix
from functions.createprefix import create_prefix
from functions.menusucursales import menu_sucursales
from functions.pingpong import pingpong
from functions.readsucursales import sucursales
from functions.threadconfig import thread_config


color_reset = "\x1b[0m"
red = "\x1b[00;00;1;031m"
red_blink = "\x1b[00;00;05;031m"
magent = "\x1b[00;00;02;033m"
magent_blink = "\x1b[00;00;02;033m"
blue = "\x1b[00;00;1;034m"
blue_blink = "\x1b[00;00;5;034m"
green = "\x1b[00;00;01;092m"
green_blink = "\x1b[00;00;5;092m"


def main():
    """
    Funcion Principal.

    Esta funcion llama a las demas funciones de la carpeta 'functions'.

    Si el resultado es exitoso se guarda en un archivo de texto, de no ser asi
    sino solo se anuncia que no tiene conectividad.
    """
    clean_screen()
    sucursales_list = sucursales()

    menu_sucursales(sucursales_list)

    try:
        creacion_prefijos = create_prefix()
        print(creacion_prefijos)

        dictionary_prefijos = dictionary_prefix(
                                        creacion_prefijos, sucursales_list
                                        )

        for index in dictionary_prefijos:
            dictionary_sucursal = index

            for (key, value) in dictionary_sucursal.items():
                print(key, len(value))
                print(f" {green}{'='*66}{color_reset}")
                print(
                    f" {blue}Realizando {green}PING {blue}a los dispositivos"
                    + f" de {green}'{key}'{color_reset}")
                print(f" {green}{'='*66}{color_reset}")

                thread_config(pingpong, value)
                print(f" {green}{'='*66}{color_reset}\n")

    except UnboundLocalError:
        print(f"{green}{'Fin del programa.':^40}{color_reset}\n\n")


if __name__ == '__main__':
    main()
