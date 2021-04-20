#4 Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

import re
texto1 = open("/Users/pilarfeijoo/Downloads/UCEMA_Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt", "r")

text = texto1.read()
palabras = text.split()

print('La cantidad de palabras en el texto son: ', len(palabras))