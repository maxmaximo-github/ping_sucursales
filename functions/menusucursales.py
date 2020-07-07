#!/usr/bin/env  python3
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020, Reboot IPv4 Phones"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.0.2"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguez@gmail.com"
__status__ = "Development"


color_reset = "\x1b[0m"
red = "\x1b[00;00;1;031m"
red_underline = "\x1b[00;00;5;031m"
green = "\x1b[00;00;01;092m"
green_underline = "\x1b[00;00;5;092m"
blue = "\x1b[00;00;1;034m"
yellow = "\x1b[00;00;02;033m"
# blue = "\x1b[00;00;03;034m"


def menu_sucursales(sucursales_list):
    """
    Buenos dias.

    Las cosas como son.
    """
    print(f"{green}{'='*45}{color_reset}")
    print(
        f"{' '*4}{red}{'SUCURSALES':^20} "
        + f"  {blue}{'PREFIJOS':^20}{color_reset}")
    print(f"{green}{'='*45}{color_reset}")
    count = 0
    for sucursal in sucursales_list:
        print(
            f"{yellow}{count}) {red}{sucursal['Sucursal']:^20} {green}==>"
            + f"{blue}{sucursal['Prefijo']:^20}")
        count += 1
    print(
        f"{yellow}{'-'}) {red}{'Todas':^20} {green}==>"
        + f" {blue}{'*':^20}{color_reset}")
    print(f"{green}{'='*45}{color_reset}\n")

    print(
        f"{red}Si deseas {blue}reiniciar {red}varias sucursales separa por "
        + f"{blue}coma {green}','{color_reset}")
    print(f"\t{blue}Example:{green} 0, 3, 5{color_reset}\n")
    print(
        f"{red}Si deseas un {blue}rango {red}utiliza {green}'-'{color_reset}")
    print(f"\t{blue}Example:{green} 1-3, 5{color_reset}\n")
    print(f"{red}Para {blue}Todas {red}las sucursales {green}'Inicial-Final'")
    fin = len(sucursales_list) - 1
    print(f"\t{blue}Example: {green}0-{fin}{color_reset}\n")
