
def verificarNumero(num):
    if(num%2==0):
        return "par"
    else:
        return "impar"

def problema2():
    print("Problema 2: Conocer si un número es par o impar")
    while True:
        num = input("Ingrese un número entero:  ")
        try:
            int(num)
            break
        except ValueError:
            print("Recuerde que solo se acepta números enteros")

    resp = verificarNumero(int(num))
    print("El número que usted ingreso es: "+ resp)

# para ejecutar el programa solo debe borrar este comentario y dejar lo siguiente: problema2()