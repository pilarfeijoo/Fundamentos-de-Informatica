#Creá un programa que declare una lista y la vaya llenando de números leídos por teclado hasta que se introduzca un número negativo. Una vez hecho esto se deben imprimir los elementos de la lista.

n = int(input("Ingrese un numero:"))
lista = []
lista.append(n)
while n >= 0:
    n = int(input("ingrese un numero:"))
    if n > 0:
        lista.append(n)
    else:
        print(list(lista))