#Creá una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copiá los elementos de la lista en otra lista pero en orden inverso, imprimí los elementos de esta última lista.
lista = []

a1 = input("dame un elemento:")
a2 = input("dame un elemento:")
a3 = input("dame un elemento:")
a4 = input("dame un elemento:")
a5 = input("dame un elemento:")
lista=[a1,a2,a3,a4,a5]

for item in lista [::-1]:
    print(item)
