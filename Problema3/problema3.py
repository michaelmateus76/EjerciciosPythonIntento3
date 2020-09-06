
def calcularDescuento(precio,dia):
    cont = -1
    aux = [10,5,3,1,7,0,1,"lunes","martes","miércoles","jueves","viernes","sábado","domingo"]
    for i in ["l","m","M","j","v","s","d"]:
        cont = cont + 1
        if i==dia:
            day = aux[cont+7] 
            por = aux[cont]
            des = precio * (aux[cont]/100)
            pre = precio - des
            break
    return day,por,des,pre

def problema3():
    print("Problema 3: Cálculo del descuento según el día de la semana")

    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if (precio<0):
                float("error")
            break
        except ValueError:
            print("Recuerde que el precio debe ser un número real positivo")

    while True:
        print("Tenga en cuenta que: Lunes: l, Martes: m, Miércoles: M, Jueves: j, Viernes: v, Sábado: s, Domingo: d")
        dia = input("Ingrese el día de la semana:  ")
        if not dia in ["l", "m","M","j","v","s","d"]:
            print("Vuelva a intentar.")
        else:
            break

    descuento = calcularDescuento(float(precio),dia)
    print("Su descuento el día "+descuento[0]+" será del "+ str(descuento[1]) +"% es decir un descuento de $"+str(descuento[2])+", precio con descuento: $"+str(descuento[3]))

# para ejecutar el programa solo debe borrar este comentario y dejar lo siguiente: problema3()