# Escribí un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena 
# (considerar que las mayúsculas difieren de las minúsculas, por lo que, si el string es "Agua", el carácter "A" tiene 1 aparición
#  y el carácter "a" también tiene 1).


contadores = {}
cadena = input("Escribi una cadena: ")
for caracter in cadena:
    if caracter in contadores:
        contadores[caracter]+=1
    else:
        contadores[caracter]=1


for clave, valor in contadores.items():
    print(clave,valor)

#print(contadores)

import string, re

abc = list(string.ascii_uppercase)
abc += list(string.ascii_lowercase)

#print(abc)

dic = {}
dic1 = {}
texto = "Agustin"

for i in abc:
    if len(re.findall(i, texto)) > 0:
        dic[i]=len(re.findall(i, texto))

print(dic)

#Con los 0
for i in abc:
    dic1[i]=len(re.findall(i, texto))

print(dic1)