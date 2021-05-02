import re

with open(r"..\UCEMA_Fundamentos_de_informatica\Python_intro\verso4.txt", "r") as texto:

    text = texto.read()
    palabras = text.split()
    print(palabras)
    lista = []
    print(len(text.split()))

    for i in palabras:
        repeticiones = palabras.count(i) #me imprime todas las palabras de split, osea las repetidas incluso. Usa 29
        #print(repeticiones)
        lista.append((repeticiones) / len(palabras))
        print(i)
    
    for frecuencias in lista:
        print(frecuencias)
        
print(lista)
#En y en las toma como palabras distintas

#OPCION 2
with open(r"..\UCEMA_Fundamentos_de_informatica\Python_intro\verso4.txt", 'r') as file:
    texto = file.read()
    palabras = texto.split()
    # palabras_sin_coma = []
    # for i in palabras:
    #     palabra = i.strip(",")
    #     palabras_sin_coma.append(palabra)

    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    for key in frecuencias:
        frecuencia1 = float('{:.4f}'.format(frecuencias[key] / len(palabras)))
        print("La palabra "+ "'" +str(key) + "'" + " tiene una frecuencia de " + str(frecuencia1))


    # print(palabras_sin_coma)
    print(frecuencias)
    print(len(frecuencias))
    #al ser total 27 ene l dic, cambia los numeros. Tomar total del split.
    print(len(palabras))