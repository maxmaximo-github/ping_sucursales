#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is create for general propouse.

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

import paramiko
import time


# Colores para impresion de pantalla.
color_reset = "\x1b[0m"
red = "\x1b[00;00;1;031m"
green = "\x1b[00;00;1;092m"
blue = "\x1b[00;00;1;034m"


def restart_phone(ip, data_info):
    """
    Funcion para reiniciar los telefonos de la sucursal en turno..

    Esta funcion reinicia los telefonos IP de las sucursales que pueden
    ser alcanzados por SSH utilizando la libreria 'Paramiko'.
    """
    # ip_address = ip
    username, password = data_info

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(
        hostname=ip,
        username=username,
        password=password
    )

    remote_connection = ssh_client.invoke_shell()

    remote_connection.send("reboot\n")

    time.sleep(1)
    output = remote_connection.recv(65535)
    output = str(output)

    if "Welcome" in output:
        print(
            f"\t{green}Rebooting {blue}Grandstream GXP2135"
            + f" {red}with {green}{ip}.")

    ssh_client.close()
