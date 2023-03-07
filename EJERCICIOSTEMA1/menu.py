"""MENU DEL PROGRAMA"""

import os

def loop():

    while True:
        
        HELPERS.clear()
        
        
        print("=============================")
        print("BIENVENIDO AL MENU PRINCIPAL")
        print("=============================")
        print("[1]RESOLVER EJERCICIO 1")
        print("[2]RESOLVER EJERCICIO 2")
        print("[3]RESOLVER EJERCICIO 3")
        print("[4]RESOLVER EJERCICIO 4")
        print("[5]RESOLVER EJERCICIO 5")
        print("[6]RESOLVER EJERCICIO 6")
        print("[7]RESOLVER EJERCICIO 7")
        print("[8]SALIR")
        print("=============================")

        opcion = input("Elige una opcion: ")

        HELPERS.clear()

        if opcion == "1":
            print("Resolviendo ejercicio 1\n")

        if opcion == "2":
            print("Resolviendo ejercicio 2\n")

        if opcion == "3":
            print("Resolviendo ejercicio 3\n")

        if opcion == "4":   
            print("Resolviendo ejercicio 4\n")

        if opcion == "5":
            print("Resolviendo ejercicio 5\n")

        if opcion == "6":
            print("Resolviendo ejercicio 6\n")

        if opcion == "7":
            print("Resolviendo ejercicio 7\n")

        if opcion == "8":
            print("Saliendo del programa\n")
            break

        input("\nPulsa ENTER para continuar...")
