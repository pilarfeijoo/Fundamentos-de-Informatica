# Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra 
# (por ejemplo que imprima cuántas líneas no empiezan con "P").

import re
with open(r"..\UCEMA_Fundamentos_de_informatica\Python_intro\manipulacion_archivos.txt", "r") as texto:
    lineas = texto.readlines()
    contador = 0
    for i in lineas:
        if re.search("^[^M]", i) is not None:
            contador += 1

    print(contador)

#OTRA FORMA DE ACCEDER A LAS LINEAS, son un elementos distintos dentro del texto sin necesidar de hacer una lista, 
#entonces podemos usar el for directamente del texto
with open(r"..\UCEMA_Fundamentos_de_informatica\Python_intro\manipulacion_archivos.txt", "r") as texto:
    contador = 0
    for i in texto:
        print(i[0])
        
       
       
  
    