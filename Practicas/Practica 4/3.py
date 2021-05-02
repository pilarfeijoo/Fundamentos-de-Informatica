# Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.

import re

with open(r"..\UCEMA_Fundamentos_de_informatica\Python_intro\manipulacion_archivos.txt", "r") as texto:
 lista = []
 for i in texto:
     lista.append(i)

print(lista[-5:])
     
#Opcion 2
with open(r"..\UCEMA_Fundamentos_de_informatica\Python_intro\manipulacion_archivos.txt", "r") as texto:
    def leer_ultimassNlineas(n):
        lineas = texto.readlines()
        print(lineas[-n:])
    
    leer_ultimassNlineas(5)