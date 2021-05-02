# Escribí un programa que lea un archivo e imprima las primeras n líneas.
import re

with open(r"..\UCEMA_Fundamentos_de_informatica\Python_intro\manipulacion_archivos.txt", "r") as texto:
    def leer_primerasNlineas(n):
        n = 0
        while n<5:
            print(texto.readline())
            n+=1

    leer_primerasNlineas(5)

