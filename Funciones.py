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

#guardar
def guardar(codigo, titulo, autor, precio):

    if None in libros:
        for i in range(10):
            if libros[i,0]==None:
                libros[i,0]=codigo
                libros[i,1]=titulo
                libros[i,2]=autor
                libros[i,3]=precio
                printv("Libro guardado")
                break


#buscar
def buscar(librob):
    for i in range(10):
        if librob in libros[i,0]:
            printv(f"CD:{i,0}, titulo:{i,1},autor:{i,2}, precio{i,3}")
        else:
            printr("El libro no esta en nuestra tienda")
    

#certificadoscriticas

#certificadodetalles
