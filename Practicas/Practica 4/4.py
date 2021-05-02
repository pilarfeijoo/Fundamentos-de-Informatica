#Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

import re

with open(r"..\UCEMA_Fundamentos_de_informatica\Python_intro\manipulacion_archivos.txt", "r") as texto:
    text = texto.read()
    print(len(re.findall("\W\w*\W", text))) #\b??
    print(re.findall("\W\\w*\W", text))



with open(r"..\UCEMA_Fundamentos_de_informatica\Python_intro\manipulacion_archivos.txt", "r") as texto:
    text = texto.read()
    palabras = text.split()
    print('La cantidad de palabras en el texto son: ', len(palabras))


