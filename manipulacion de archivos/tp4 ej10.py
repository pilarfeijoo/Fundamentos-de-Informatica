#10 Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una determinada carpeta.


"/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt"
import re

#creamos nuevo archivo
menjunje = open('menjunje.txt', 'w')

#copiamos la info de la carpeta: /Users/guti/Documents/menjunje de textos
with open("/Users/pilarfeijoo/Downloads/menjunje de textos/bio.txt") as f:
    with open("/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt", "w") as f1:
        for line in f:
            f1.write(line)

with open("/Users/pilarfeijoo/Downloads/menjunje de textos/Copia de lectura_escritura.py") as f:
    with open("/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt", "a") as f1:
        for line in f:
            f1.write(line)

with open("/Users/pilarfeijoo/Downloads/menjunje de textos/readme.txt") as f:
    with open("/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt", "a") as f1:
        for line in f:
            f1.write(line)

