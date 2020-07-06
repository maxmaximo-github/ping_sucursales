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
import glob
from os import remove


def remover_files():
    directory = os.getcwd()
    for file_name in glob.glob(("{}/tmp/*").format(directory)):
        remove(file_name)
