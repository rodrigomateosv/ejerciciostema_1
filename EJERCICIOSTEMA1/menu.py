"""MENU DEL PROGRAMA"""

import os
import sys
from ejercicio7 import agregar_una_vez
from ejercicio1 import Alumno
import helpers
from ejercicio2 import *
from ejercicio3 import *
from ejercicio4 import *
from ejercicio6 import *
from ejercicio5 import *
from ejercicio7 import *
import ejercicio2
import _init_

_init_(autoreset=True)

def loop():

    while True:
        
        helpers.clear()
        
        
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

        helpers.clear()

        if opcion == "1":
            print("Ejercicio 1: Alumno\n")
             #ejercicicios.alumno
            Alumno.cadena=input("Ingresa tu cadena corrupta: ", )
            print(Alumno.transformar_cadena(Alumno.cadena))
         

        if opcion == "2":
             print("Ejercicio 2: Número mágico\n")
             n = int(input("Ingresa un número: "))
             print(ejercicio2.numero_magico.num(n))



        if opcion == "3":
            print("Ejercicio 3: Listas\n")
            list1 =list(input("Ingresa tu primera lista: "))
            list2 =list(input("Ingresa tu segunda lista: ", ))
            print(lista(list1, list2))


        if opcion == "4":   
            print("Ejercicio 4: Tareas\n")
            list_cola=[]
            NumeroTareas = int(input("Ingresa el número de tareas: ", ))
            for i in range(NumeroTareas):
                # Crear un diccionario
                cola = {}
                # Agregar elementos al diccionario
                cola[f'tarea {i+1}'] = input(f'Ingresa la tarea {i+1}: ', )
                cola[f'prioridad'] = input(f'Ingresa la prioridad de la tarea {i+1}: ', "blue")
                list_cola.append(cola)
            estructura_cola(list_cola)

        if opcion == "5":
            print("Ejercicio 5: Descomposicion\n") 
            n=input("Ingresa un número: ", )
            descomponer(n)


        if opcion == "6":
            print("Ejercicio 6: Pares e impares\n")
            n=int(input("Longitud de la lista: ", ))
            lista6=[]
            for i in range(n):
                lista6.append(int(input("Ingresa el número: ", "blue")))
            print(separar(lista6))



        if opcion == "7":
            print("Ejercicio 7: Agregar una vez\n")
            # lista por inputs con ints y strings
            lista7= []
            n = int(input("Longitud de la lista: ", ))
            for i in range(n):
                lista7.append(input("Ingresa el elemento de la lista: ", "blue"))
                if lista7[i].isnumeric():
                    lista7[i] = int(lista7[i])
            elemento = input("Ingresa el elemento: ", )
            print(agregar_una_vez(lista7, elemento))

        if opcion == "8":
            print("Saliendo del programa\n")
            break

        input("\nPulsa ENTER para continuar...")


(loop())
