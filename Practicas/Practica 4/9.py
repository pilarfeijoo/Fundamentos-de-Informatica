#Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. Recordá que la frecuencia es la relación 
# entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.

import re
#OTRO TEXTO r"..\UCEMA_Fundamentos_de_informatica\Python_intro\manipulacion_archivos.txt"

#OPCION3
with open(r"..\UCEMA_Fundamentos_de_informatica\Python_intro\verso4.txt") as texto:
    text = texto.read()
    palabras = text.split()
    print(len(palabras))

    lista_palabras_unicas = []
    for i in palabras:
        if i not in lista_palabras_unicas:
            lista_palabras_unicas.append(i)

    print(lista_palabras_unicas)
    
    suma = 0
    for i in lista_palabras_unicas:
        #print(re.findall(i, text))
        repeticiones =len(re.findall(i, text))
        frecuencia = float('{:.4f}'.format(repeticiones / len(palabras)))
        print("La frecuencia de " + "'" +str(i) +"'"+ " es: " + str(frecuencia)) 
        
        suma += frecuencia


print(suma)
