
def calcularEdad2070(edadPresente,añoActual):
    edadFuturo = int(edadPresente) + (2070 - int(añoActual))
    return edadFuturo

def problema1():
    print("Problema 1: Cálculo de la edad que tendrá en el año 2070")
    while True:
        edadActual = input("Ingrese su edad actual:  ")
        try:
            int(edadActual)
            if(int(edadActual)>0):
                break
            else:
                print("Solo se acepta números positivos")
        except ValueError:
            print("Recuerde que solo se acepta números enteros")


    while True:
        añoActual = input("Ingrese el año actual:  ")
        try:
            int(añoActual)
            if(int(añoActual)>0 and int(añoActual)<2070):
                break
            else:
                print("Solo se acepta numeros positivos menores a 2070")
        except ValueError:
            print("Recuerde que solo se acepta números enteros")

    edad2070 = calcularEdad2070(edadActual,añoActual)
    print("Su edad en el año 2070 será de: "+ str(edad2070) + " años")

# para ejecutar el programa solo debe borrar este comentario y dejar lo siguiente:  problema1()