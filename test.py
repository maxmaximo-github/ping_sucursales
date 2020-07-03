#!/usr/bin/env  python3


ingresa = "2-4"

creacion_prefijos = []
if "-" in ingresa:
    datos_prueba = ingresa.split("-")

    datos = []
    for x in datos_prueba:
        x = int(x)
        print(x)
        print(type(x))
        datos.append(x)

    inicio = datos[0]
    longitud = datos[-1] + 1
    print(longitud)

    for x in range(inicio, longitud, 1):
        creacion_prefijos.append(x)

print(creacion_prefijos)