


edades = [20,5,4,3,20,20]


def edad_repetida(lista):
    for lugar in lista:
        if lugar==max(lista):
            print(list.index(lista, lugar))



edad_repetida(edades)
