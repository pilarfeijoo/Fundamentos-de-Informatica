#9. Escribí un programa que extraiga los caracteres que estén entre guiones en un string. 
# (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")
import re 
string = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
patron = "-(.*?)-"
a = re.findall(patron, string)

#Cuando se refiere a caracteres no se si quiere la palabra o los caracteres sueltos
print(a)
for i in a:
    for i in i:
        print(i)