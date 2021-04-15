#Escribí un programa que lea un archivo e imprima las primeras n líneas.

import re
texto1 = open("/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt", "r")


n = 0

while n <= 5 :
    n +=1
    print(texto1.readline())