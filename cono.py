#!/usr/bin/python3
# Created by: Programing_Hackers
from pyfiglet import Figlet
import time
import sys
import os
os.system('clear')
def cono():
    f = Figlet(font='slant')
    print ("\033[35m")
    print (f.renderText('    EL CONO'))
    print ("\033[36m")
    time.asctime()
    print("*" * 23)
    print ("""
            MENU
    1] AREA LATERAL
    2] AREA TOTAL
    3] VOLUMEN
    4] SALIR
    """)
    print("*" * 23)
    op = int(input("Elija una opcion: "))
    while op <= 0 or op >= 5:
        op = int(input("Elija una opcion correcta: "))
    if op == 1:
        print ("AREA LATERAL")
        pi = 3.14
        r = float(input("Ingrese el valor del radio: "))
        g = float(input("Ingrese el valor de la generatriz: "))
        al = r * g * pi
        print ("El area lateral es: {}".format(round(al, 2)))
        input("Pulse ENTER para continuar")
        time.sleep(0.8)
        os.system('clear')
        cono()
    elif op == 2:
        print("AREA TOTAL")
        pi = 3.14
        r = float(input("Ingrese el valor del radio: "))
        g = float(input("Ingrese el valor de la generatriz: "))
        at = pi * r * (r + g)
        print ("El area total es: {}".format(round(at, 2)))
        input("Pulse ENTER para continuar")
        time.sleep(0.8)
        os.system('clear')
        cono()
    elif op == 3:
        print ("Volumen")
        pi = 3.14
        r = float(input("Ingrese el valor del radio: "))
        h = float(input("Ingrese el valor de la altura: "))
        v = (1 / 3) * (pi * (r ** 2) * h)
        print ("El volumen es: {}".format(round(v, 2)))
        input("Pulse ENTER para continuar")
        time.sleep(0.8)
        os.system('clear')
        cono()
    else:
        time.sleep(0.5)
        os.system("clear")
        print ("Gracias")
        print ("Vuelva Pronto :3")
        sys.exit()
if __name__ == "__main__":
    cono()
