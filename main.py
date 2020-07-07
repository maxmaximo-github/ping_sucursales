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


from functions.createtmpfolder import create_tmpfolder
from functions.cleanscreen import clean_screen
from functions.countdown import count_down
from functions.dictionaryprefix import dictionary_prefix
from functions.createprefix import create_prefix
from functions.menusucursales import menu_sucursales
from functions.pingpong import ping_pong
from functions.readfiles import read_files
from functions.readsucursales import sucursales
from functions.remover import remover_files
from functions.restartphone import restart_phone
from functions.sshalive import ssh_alive
from functions.threadconfig import thread_config


# Colores para impresion en pantalla.
color_reset = "\x1b[0m"
red = "\x1b[00;00;1;031m"
red_blink = "\x1b[00;00;05;031m"
magent = "\x1b[00;00;02;033m"
magent_blink = "\x1b[00;00;05;033m"
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
    # Verificar si existe carpeta tmp dentro del proyecto
    create_tmpfolder()

    # Limpiar pantalla
    clean_screen()

    # Obtener esctructura de datos para el menu
    sucursales_list = sucursales()
    # print(sucursales_list)

    # Impresion de pantalla el menu con sus sucursales y prefijos.
    menu_sucursales(sucursales_list)

    try:
        creacion_prefijos = create_prefix()
        # Limpiar pantalla
        clean_screen()

        dictionary_prefijos = dictionary_prefix(
                                        creacion_prefijos, sucursales_list
                                        )

        for index in dictionary_prefijos:
            dictionary_sucursal = index

            for (key, value) in dictionary_sucursal.items():

                # Impresion de formato para la terminal
                print(f" {green}{'='*66}{color_reset}\n")
                print(
                    f"\t {blue}Conectando {red}con la sucursal "
                    + f"{green}'{key}'\n")
                print(f"{red}{'*'*55:^66}{color_reset} ")
                print(
                    f"      {blue}Realizando {green}PING "
                    + f"{blue}a los {red}Telefonos de"
                    + f" {green}'{key}' {color_reset}\n")
                # Llamada a la funcion "thread_config" para la creacion de los
                # hilos y determinar que dispositivos son alcanzados por
                # ping
                thread_config(ping_pong, value)
                # Impresion de formato para la terminal.
                print(f"{red}{'*'*55:^66}{color_reset} ")

                # Leer los archivos de los dispositivos que se encuentran
                # activos.
                devices_ssh = read_files()

                # Remover archivos temporales con las IP
                remover_files()

                # Impresion de formato para la terminal
                print(f"\n{red}{'*'*55:^66}{color_reset} ")
                print(
                    f"\t{blue} Probando {red}conectividad "
                    + f"{green}SSH {red}con {green}'{key}' {color_reset}\n")

                # Llamada a la funcion "thread_config" para la creacion de los
                # hilos y determinar que dispositivos son alcanzados por SSH
                thread_config(ssh_alive, devices_ssh)

                # Impresion de formato para la terminal
                print(f"{red}{'*'*55:^66}{color_reset} ")

                # Leer los archivos de los dispositivos que se encuentran
                # activos SSH.
                devices_configuration = read_files()

                # Impresion de formato para la terminal
                print(f"\n{red}{'*'*55:^66}{color_reset} ")
                print(
                    f"\t\t{blue} Reiniciando Telefonos "
                    + f"{green}'{key}'{color_reset}")

                # Llamada a la funcion "thread_config" para la creacion de los
                # hilos y determinar que dispositivos son alcanzados por SSH
                thread_config(restart_phone, devices_configuration)
                # Impresion de formato para la terminal
                print(f"{red}{'*'*55:^66}{color_reset} ")
                print(f" {green}{'='*66}{color_reset}\n\n\n")

                # Limpiar archivos de la carpeta temporal para la siguiente
                # ejecution.
                remover_files()

        # Impresion de formato para la terminal.
        print(f" {green}{'='*66}")
        print(
            f"  {red}Esperando {green}reinicio {red}para comprobar"
            + f" la {green}conectividad {red}con "
            + f"{green}Telefonos.{magent_blink}")

        # Llamada a la funcion count_down y pasarle argumentos con valores
        # de ejemplo minutos=2 y segundo=0
        count_down(minutes=0, seconds=5)

        # Impresion de formato para la terminal.
        print(f" {green}{'='*66}\n\n\n")

        # Realizar ping nuevamente para determinar que los telefonos
        # Ya son disponibles
        for index in dictionary_prefijos:
            dictionary_sucursal = index

            for (key, value) in dictionary_sucursal.items():

                print(f" {green}{'='*66}{color_reset}\n")
                print(
                    f"\t {blue}Conectando {red}con la sucursal "
                    + f"{green}'{key}'\n")
                print(f"{red}{'*'*55:^66}{color_reset} ")
                print(
                    f"      {blue}Realizando {green}PING "
                    + f"{blue}a los {red}Telefonos de"
                    + f" {green}'{key}' {color_reset}\n")

                # Llamada a la funcion "thread_config" para la creacion de los
                # hilos y determinar que dispositivos son alcanzados por
                # ping
                thread_config(ping_pong, value)

                # Impresion de formato para la terminal.
                print(f"{red}{'*'*55:^66}{color_reset} ")
                print(f" {green}{'='*66}{color_reset}")

    except KeyboardInterrupt:
        print(
            f"\n\n\t{red}Has detenido el {green}programa {red}con el teclado.")

    except UnboundLocalError:
        print()

    finally:
        print(f"{green}{'Fin del programa':^60}{color_reset}\n")
        print(f" {red}{'*'*66}")
        print(
            f"      {blue}Desarrollado y mantenido"
            + f" por: {green}Ing. {__author__}")
        print(f"\t    {blue}Contacto: {green}{__email__}")
        print(f"\t\t        {blue}Version: {green}{__version__}")
        print(f" {red}{'*'*66}{color_reset}\n\n")


if __name__ == '__main__':
    main()
