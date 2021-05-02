#Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

import re

#copiamos la info del viejo en el nuevo
with open(r"..\UCEMA_Fundamentos_de_informatica\Python_intro\manipulacion_archivos.txt") as f:
    with open(r".\Practicas\Practica 4\text.txt", "w") as f1: #creamos el nuevo para poder copiar la inof
        for line in f:
            f1.write(line)

#modificamos la info
nuevo = open(r"..\UCEMA_Fundamentos_de_informatica\Python_intro\manipulacion_archivos.txt", "r+")

nuevotext = nuevo.read()
nuevotext = re.sub("p", "p\n", nuevotext)

with open(r".\Practicas\Practica 4\text.txt", "w") as file:
    file.write(nuevotext)

nuevo.close()