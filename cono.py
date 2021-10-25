#!/usr/bin/python3
# Programa para lo que sea xD

from pyfiglet import Figlet
import time
import sys
import os

def cono():
    f = Figlet(font='slant')
    print ("\033[35m")
    print (f.renderText('    EL CONO :V'))
    print ("\033[36m")
    print ("""
            MENU
    1] AREA LATERAL
    2] AREA TOTAL
    3] VOLUMEN
    4] SALIR
    """)
    op = int(input("Elija una opcion: "))
    while op <= 0 or op >= 5:
        op = int(input("Elija una opcion correcta: "))
    if op == 1:
        print ("AREA LATERAL")
        pi = 3.14
        r = int(input("Ingrese el valor del radio: "))
        g = int(input("Ingrese el valor de la generatriz: "))
        al = r * g * pi
        print ("El area lateral es: {}".format(al))
    elif op == 2:
        print("AREA TOTAL")
        pi = 3.14
        r = int(input("Ingrese el valor del radio: "))
        g = int(input("Ingrese el valor de la generatriz: "))
        at = pi * r (r + g)
        print ("El area total es: {}".format(at))
    elif op == 3:
        print ("Volumen")
        pi = 3.14
        r = int(input("Ingrese el valor del radio: "))
        h = int(input("Ingrese el valor de la altura: "))
        v = (1 / 3) * (pi * (r ** 2) * h)
        print ("El volumen es: {}".format(v))
    else:
        time.sleep(0.5)
        os.system("clear")
        print ("Gracias")
        print ("Vuelva Pronto :3")
        sys.exit()
cono()
