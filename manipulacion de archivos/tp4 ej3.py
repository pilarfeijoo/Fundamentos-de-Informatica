#Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.

import re
texto1 = open("/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt", "r")


n = 0

while n <= 5 :
    n +=1
    print(texto1.readline())