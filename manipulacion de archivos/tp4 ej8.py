#8 Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

import re

#creamos nuevo archivo para cargarle la info
nuevo = open('conjunto.txt', 'w')


#copiamos la info del primero en el nuevo (en este caso el poema)
with open("/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt") as f:
    with open("/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt", "w") as f1:
        for line in f:
            f1.write(line)

#copiamos la info del segundo en el nuevo (en este caso la bio) (usamos 'a' xq sino lo sobreescribe)
with open("/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt") as f:
    with open("/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt", "a") as f1:
        for line in f:
            f1.write(line)
