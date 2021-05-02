#Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

#creamos nuevo archivo
nuevo = open('text3.txt', 'w')

#copiamos la info del viejo en el nuevo
with open(r"..\UCEMA_Fundamentos_de_informatica\Python_intro\manipulacion_archivos.txt") as f:
    with open(r'.\Practicas\Practica 4\text1.txt', "w") as f1:
        for line in f:
            f1.write(line)

#modificamos la info
tercero = open(r'.\Practicas\Practica 4\text1.txt', "r+")

tercerotext = tercero.read()
tercerotext = tercerotext.replace('\n',' ')

with open(r'.\Practicas\Practica 4\text1.txt', 'w') as file:
  file.write(tercerotext)