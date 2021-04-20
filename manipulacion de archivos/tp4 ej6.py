#7 Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

import re

#creamos nuevo archivo
nuevo = open('text3.txt', 'w')

#copiamos la informacion del viejo en el nuevo
with open("/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt") as f:
    with open("/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt", "w") as f1:
        for line in f:
            f1.write(line)

#modificamos la informacion
tercero = open("/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt", "r+")


tercerotext = tercero.read()

tercerotext = tercerotext.replace('\n',' ')

with open("/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt", 'w') as file:
  file.write(tercerotext)
