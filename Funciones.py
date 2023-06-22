from colorama import Style, Fore, Back
import os
import msvcrt
import random
import numpy

#######################################
#CREAR ARREGLOS
libros=numpy.empty([10,4], object)
#######################################
#FUNCIONES DE DISEÑO
def printv(texto):
    print(f"{Fore.GREEN}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")

def printr(texto):
    print(f"{Fore.RED}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")

def limpiarpantalla():
    printv("<<<PRESIONE TECLA PARA CONTINUAR>>>")
    msvcrt.getch()
    os.system('CLS')
#######################################
#funciones de arreglo
#validarcodigo

#guardar

#buscar

#certificadoscriticas

#certificadodetalles

#######################################
#######################################
#######################################
#######################################