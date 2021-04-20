#9 Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.

"/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt"

import re

with open("/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt", "r") as texto:
    text = texto.read()
    palabras = text.split()
    print(len(palabras))

    lista_palabras_unicas = []
    for i in palabras:
        if i not in lista_palabras_unicas:
            lista_palabras_unicas.append(i)

    print(lista_palabras_unicas)
    

    for i in lista_palabras_unicas:
        print(re.findall(i, text))
        repeticiones =len(re.findall(i, text))
        frecuencia = float('{:.4f}'.format(repeticiones / len(palabras)))
        print("La frecuencia de " + "'" +str(i) +"'"+ " es: " + str(frecuencia))

#otra manera de hacerlo

archivo = input("Que archivo deseas abrir? ")
with open(archivo, "r") as f:
    palabras = f.read().split()

buscar_palabras = input("Que palabra deseas buscar? ").split(',')
buscar_palabras = [palabra.strip().lower() for palabra in buscar_palabras]
print(buscar_palabras)
buscar_conteo = dict.fromkeys(buscar_palabras, 0)

for palabra in palabras:
    palabra = palabra.rstrip(",.").lower()
    if palabra in buscar_conteo:
        buscar_conteo[palabra] += 1

print ('\nLa frecuencia es de palabras es: ')
for palabra in buscar_palabras:
    print("{:<0s} / {} ocurrencias".format(palabra, buscar_conteo[palabra]))