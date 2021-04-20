#5 Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

import re

#creamos archivo nuevo
nuevo = open('text2.txt', 'w')


#copiamos la informacion del archivo viejo en el nuevo
with open("/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt") as f:
    with open("/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt", "w") as f1:
        for line in f:
            f1.write(line)

#modificamos la informacion
nuevo = open("/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt", "r+")


nuevotext = nuevo.read()

nuevotext = nuevotext.replace('p', 'p\n')


with open("/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt", 'w') as file:
  file.write(nuevotext)