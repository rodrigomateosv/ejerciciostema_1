"""FUNCIONES DE AYUDA"""

import os
import platform

def clear():
    """Limpia la pantalla"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")