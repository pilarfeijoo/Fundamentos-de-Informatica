#11. Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima. 
#(Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
import re
lista = ["hola Práctica sjndeui Python", "Práctica C++", "Práctica Fortran"]

for i in lista:
    patron = "(P\w*)"
    strings = re.findall(patron, i) 
    if len(strings) == 2:
        print(strings[0] + " " + (strings[1]))



#opcion 2
import re

def dos_p(lista):
    for elemento in lista:
        resultado = re.match("(P\w*)\W(P\w*)", elemento)        
        if resultado is not None:
            print(resultado.group())

lista = ["Práctica Python", "Práctica C++", "Práctica Fortran"]
dos_p(lista)
