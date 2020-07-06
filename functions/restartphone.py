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


import paramiko
import time


# Colores para impresion de pantalla.
color_reset = "\x1b[0m"
red = "\x1b[00;00;1;031m"
green = "\x1b[00;00;1;092m"
blue = "\x1b[00;00;1;034m"


def restart_phone(ip):
    """
    Funcion para reiniciar los telefonos de la sucursal en turno..

    Esta funcion reinicia los telefonos IP de las sucursales que pueden
    ser alcanzados por SSH utilizando la libreria 'Paramiko'.
    """
    # ip_address = ip
    username = "admin"
    password = "hyc.2016!Trc"

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
    print(output)

    ssh_client.close()
