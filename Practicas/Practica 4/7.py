#Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres
# tiene.

import re

with open(r".\Teoricas\Clase 2\bio.txt") as file:
    data = file.read().split()
    palabra_max = (max(data,key=len))
    print(palabra_max)
    print(len(palabra_max))    
    
    resultado=[palabra for palabra in data if len(palabra)==len(palabra_max)]
    print(resultado)