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


def create_prefix():
    """
    Funcion para testear IPv4.

    Esta funcion realiza el testeo de Ping.

    Si el resultado es exitoso se guarda en un archivo de texto, de no ser asi
    sino solo se anuncia que no tiene conectividad.
    """
    try:
        # Usuario ingresa los valore de las sucursales.
        print(f"{green}{'='*45}")
        sucursales_usuario = input(
            f"  {red}Ingresa {green}No. {blue}de las {red}sucursales: {green}")
        print(f"{color_reset}")
        # print(sucursales_usuario)
        # print(type(sucursales_usuario))

        sucursales_usuario = sucursales_usuario.split(",")
        # print(sucursales_usuario)
        # print(len(sucursales_usuario))
        sucursales_usuario.sort()

        tmp_creacion_prefijos = []
        for no_sucursal in sucursales_usuario:
            # Si se agrega un rango Ex: 1-3 se entra en esta condicion.
            if "-" in no_sucursal:
                # Division de
                datos_test = no_sucursal.split("-")

                datos = []
                for _ in datos_test:
                    _ = int(_)
                    datos.append(_)

                start = datos[0]
                finish = datos[-1] + 1

                for _ in range(start, finish, 1):
                    tmp_creacion_prefijos.append(_)

            elif ", " in no_sucursal:
                no_sucursal = no_sucursal.split(",")
                no_sucursal = no_sucursal.strip(" ")
                no_sucursal = int(no_sucursal)
                tmp_creacion_prefijos.append(no_sucursal)

            elif " " in no_sucursal:
                no_sucursal = no_sucursal.strip(" ")
                no_sucursal = int(no_sucursal)
                tmp_creacion_prefijos.append(no_sucursal)

            elif no_sucursal.isnumeric():
                no_sucursal = int(no_sucursal)
                tmp_creacion_prefijos.append(no_sucursal)

            else:
                no_sucursal = int(no_sucursal)
                tmp_creacion_prefijos.append(no_sucursal)

        tmp_creacion_prefijos.sort()

        creacion_prefijos = []

        for data in tmp_creacion_prefijos:

            if data not in creacion_prefijos:
                creacion_prefijos.append(data)

        creacion_prefijos.sort()

    except ValueError:
        clean_screen()

        error = []
        for valor in sucursales_usuario:
            if " " in valor:
                valor = valor.strip(" ")

            if not valor.isnumeric():
                error.append(valor)

        print(f"\n{blue}{'='*60}")
        print(f"{red_blink} {('Error '*10):^40}")
        print(f"{blue}{'='*60}\n")
        print(
            f"{red}El programa {green}NO PUEDE CONTINUAR"
            + f" {red}debido a lo siguiente:{color_reset} \n")
        print(f"{red}Posiblemente ingresaste {green}'DATOS NO VALIDOS'.\n")
        print(f"{red}Tus datos que causan error son: ")
        print(f" {green}{error}{color_reset}\n")

    except KeyboardInterrupt:
        print(
            f"\n\n{red}Has detenido el {green}programa {red}con el teclado.")

    return creacion_prefijos
