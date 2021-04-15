#Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").

import re
texto1  = open("/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt", "r")

lineas = texto1.readlines()
contador = 0
print(lineas)

for i in lineas:
    if re.search("ˆ[ˆM]",i) is not None:
        contador+= 1


print(contador)
