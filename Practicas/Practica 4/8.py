#Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

import re

#creamos nuevo archivo para cargarle la info
nuevo = open(r'.\Practicas\Practica 4\conjunto.txt', 'w')


#copiamos la info del primero en el nuevo (en este caso el poema)
with open(r"..\UCEMA_Fundamentos_de_informatica\Python_intro\verso3.txt") as f:
    with open(r'.\Practicas\Practica 4\conjunto.txt', "w") as f1:
        for line in f:
            f1.write(line)

#copiamos la info del segundo en el nuevo (en este caso la bio) (usamos 'a' xq sino lo sobreescribe)
with open(r"..\UCEMA_Fundamentos_de_informatica\Python_intro\verso4.txt") as f:
    with open(r'.\Practicas\Practica 4\conjunto.txt', "a") as f1:
        f1.write("\n\n")
        for line in f:
            f1.write(line)