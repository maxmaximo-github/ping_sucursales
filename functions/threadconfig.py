#!/usr/bin/env  python3
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020, Reboot IPv4 Phones"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.0.2"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguez@gmail.com"
__status__ = "Develop"



import threading


def thread_config(function, ip_list):
    """
    Funcion para la ejecucion de hilos para la configuracion simultanea de
    dispositivos.
    """
    try:
        threads = []

        for ip in ip_list:
            th = threading.Thread(target=function, args=(ip,))
            th.start()
            threads.append(th)

        for th in threads:
            th.join()

    except KeyboardInterrupt as error:
        print(f"\nCancelaste la operacion {ip} {error}")
