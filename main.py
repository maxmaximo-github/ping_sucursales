#!/usr/bin/env  python3
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020, Reboot IPv4 Phones"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.0.2"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguez@gmail.com"
__status__ = "Develop"


from functions.cleanscreen import clean_screen
from functions.dictionaryprefix import dictionary_prefix
from functions.createprefix import create_prefix
from functions.menusucursales import menu_sucursales
from functions.pingpong import pingpong
from functions.readsucursales import sucursales
from functions.threadconfig import thread_config


color_reset = "\x1b[0m"
red = "\x1b[00;00;1;031m"
red_blink = "\x1b[00;00;5;031m"
magent = "\x1b[00;00;02;033m"
magent_blink = "\x1b[00;00;02;033m"
blue = "\x1b[00;00;1;034m"
blue_blink = "\x1b[00;00;5;034m"
green = "\x1b[00;00;01;092m"
green_blink = "\x1b[00;00;5;092m"


def main():
    # Limpiar pantalla
    clean_screen()
    sucursales_list = sucursales()

    menu_sucursales(sucursales_list)

    try:
        creacion_prefijos = create_prefix()


        dictionary_prefijos = dictionary_prefix(creacion_prefijos,
                                                sucursales_list)

        for index in dictionary_prefijos:
            dictionary_sucursal = index

            for (key, value) in dictionary_sucursal.items():
                print(f" {green}{'='*66}{color_reset}")
                print(
                    f" {blue}Realizando {green}PING {blue}a los dispositivos de "
                    + f"{green}'{key}'{color_reset}")
                print(f" {green}{'='*66}{color_reset}")

                thread_config(pingpong, value)
                print(f" {green}{'='*66}{color_reset}\n")

    except UnboundLocalError:
        print(f"{green}{'Fin del programa.':^40}{color_reset}\n\n")

if __name__ == '__main__':
    main()


# print(sucursales_list)

# data = {}
# with open(file="./sucursales/sucursales.txt", mode="r") as file:
#     for line in file:
#         line = line.rstrip("\n").strip(", ")
#         data[line[0]] = line[1]

# print(data)

#data_dictionary = {}


# for dato in data:
#    dato = dato.strip(", ")
#    print(type(dato))
    # key, value = dato[0], dato[1]
    # data_dictionary[key] = dato[1]

# print(data_dictionary)


"""
    if "," in sucursales_usuario:
        sucursales_usuario = sucursales_usuario.strip(" ")
        sucursales_usuario = sucursales_usuario.split(",")
        sucursales_usuario.sort()

    elif ", " in sucursales_usuario:
        sucursales_usuario = sucursales_usuario.strip(" ").split(", ")
        sucursales_usuario.sort()

    elif " " in sucursales_usuario:
        sucursales_usuario = sucursales_usuario.split(" ")
        sucursales_usuario.sort()




    # sucursales_usuario = sucursales_usuario.strip(" ").split(",")
    # sucursales_usuario = sucursales_usuario.split(", ")




    # sucursales_usuario = sucursales_usuario.strip().split(" ")



def menu_sucursales(sucursales_list):

    print(f"{green}{'='*45}{color_reset}")
    print(f"{' '*4}{red}{'SUCURSALES':^20}   {blue}{'PREFIJOS':^20}{color_reset}")
    print(f"{green}{'='*45}{color_reset}")
    count = 1
    for sucursal in sucursales_list:
        print(
            f"{yellow}{count}) {red}{sucursal['Sucursal']:^20} {green}==>"
            + f"{blue}{sucursal['Prefijo']:^20}")
        count += 1
    print(f"{yellow}{'*'}) {red}{'Todas':^20} {green}==> {blue}{'*':^20}{color_reset}")
    print(f"{green}{'='*45}{color_reset}\n")


sucursales_usuario = input("Ingresa las sucursales: ")

    sucursales_usuario = sucursales_usuario.split(",")
    sucursales_usuario.sort()

    tmp_creacion_prefijos = []
    for no_sucursal in sucursales_usuario:
        if "-" in no_sucursal:
            datos_test = no_sucursal.split("-")

            datos = []
            for x in datos_test:
                x = int(x)
                print(type(x))
                datos.append(x)

            start = datos[0]
            finish = datos[-1] + 1

            for x in range(start, finish, 1):
               tmp_creacion_prefijos.append(x)


        elif " " in no_sucursal:
            no_sucursal = no_sucursal.strip(" ")
            no_sucursal = int(no_sucursal)
            tmp_creacion_prefijos.append(no_sucursal)

    tmp_creacion_prefijos.sort()

    creacion_prefijos = []
    for data in tmp_creacion_prefijos:

        if not data in creacion_prefijos:
            creacion_prefijos.append(data)

    creacion_prefijos.sort()

"""


    # print(dictionary_prefijos)
    # print(len(dictionary_prefijos))
    # for x in dictionary_prefijos:
    #   dictionary_sucursal = dictionary_prefijos[x]
    #   print(dictionary_sucursal)

        #
        # for key, value in dictionary_sucursal.items():
        #    print(f" ====== Central {key} =======")
        #    ip_list = value

        #   thread_config(pingpong, ip_list)



   # print(type(dictionary_prefijos))
    # print(len(dictionary_prefijos))
    # print(type(ip_list))
    # print(ip_list)
    # print(dictionary)
    #print(type(dictionary))

    ##print(creacion_prefijos)
    ##print(len(creacion_prefijos))
    ## print(type(creacion_prefijos))
