import Funciones as fu

while True:
    fu.limpiarpantalla()
    fu.printv("Sistema VENTABOOKS")
    fu.printv("********************")
    print("1)Guardar")
    print("2)Buscar")
    print("3)Certificados")
    print("0)salir")
    opcion=int(input("Seleccione: "))

    #validamos opcion

    if opcion==0:
        fu.printv("Adios :D")
        break    
    elif opcion==1:
        fu.printv("Guardar")
        codigo=input("Ingrese codigo: ")
        titulo=input("ingrese titulo (min. 4 caracteres): ") 
        while len(titulo)<4:
            titulo=input("Ingrese titulo")
        autor=input("Ingrese nombre autor: ") 
        precio=int(input("Ingrese precio: "))
        while precio<=0:
            precio=int(input("Ingrese Precio valido: "))
        fu.guardar(codigo,titulo,autor,precio)

    elif opcion==2:
        fu.printv("Buscar")
        librob=input("ingrese codigo del libro a buscar: ")
        fu.buscar(librob)

    elif opcion==3:
        fu.printv("Certificados")
        print("1)criticas")
        print("2)Detalles")
        cert=int(input("Seleccione: "))

        if cert==1:
            fu.printv("Certificado Criticas")
        elif cert==2:
            fu.printv("Certificado de ventas")
        else:
            fu.printr("Opcion no valida")

    
    else:
        fu.printr("Opcion no valida")
        
