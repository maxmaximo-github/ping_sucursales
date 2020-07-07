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


import time


# Colores para impresion en pantalla.
color_reset = "\x1b[0m"
red = "\x1b[00;00;1;031m"
red_blink = "\x1b[00;00;05;031m"
magent = "\x1b[00;00;02;033m"
magent_blink = "\x1b[00;00;02;033m"
blue = "\x1b[00;00;1;034m"
blue_blink = "\x1b[00;00;5;034m"
green = "\x1b[00;00;01;092m"
green_blink = "\x1b[00;00;5;092m"


def count_down(minutes, seconds):
    """
    Funcion contador de minutos y segundos.

    Esta funcion crea un contador decendente para indicarle al usuario en
    cuanto se volvera a realizar las pruebas de conectividad.
    """
    k = 0
    while True:

        if seconds == -1:
            seconds = 59
            minutes -= 1

        if seconds > 9:
            print(
                "\t\t\t\t" + str(k) + str(minutes) + ":"
                + str(seconds), end="\r")

        else:
            print(
                "\t\t\t\t" + str(k) + str(minutes) + ":"
                + str(k) + str(seconds), end="\r")

        time.sleep(1)

        seconds -= 1

        if minutes == 0 and seconds == -1:
            break

    if minutes == 0 and seconds == -1:
        print(
            f"\t\t     {red_blink}!!!{green_blink}Telefonos"
            + f" reiniciados{red_blink}!!!!")
        time.sleep(1)
