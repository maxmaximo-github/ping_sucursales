#!/usr/bin/env  python3
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020, Reboot IPv4 Phones"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.0.2"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguez@gmail.com"
__status__ = "Develop"


from os import name
from os import system


def clean_screen():
        if name == "nt":
            _ = system("cls")

        else:
            _ = system("clear")
            # print("Tienes {}".format(name))
