
import re
#En las rutas de windows puedo usar doble \\ o r\ para que python la tome literal y no como un escape.

#Desafio I Creá un archivo de prueba (bio.txt) en la carpeta destinada a los prácticos de la materia.
texto = open(r"C:\Users\agust\Desktop\UCEMA\Informatica\Repositorio_Informatica\Teoricas\Clase 2\bio.txt","a")

#2da forma de abrir archivo, mas segura porque lo cierra solo
# with open(path_al_archivo, modo) as miarch:
    #Aquí van las líneas de procesamiento del archivo

#miarch es modificable lo puedo nombrar como quiera, es la variable que luego puedo usar para llamar al archivo

# Desafío II: Investigá sobre los métodos os.mkdir() y os.listdir()   
#os.mkdir() crea un nuevo directorio dentro del que estoy
# os.listdir() me dice todos los archivos que hay en ese directorio

import os
print(os.getcwd())

os.chdir('C:\\Users\\agust\\Desktop\\UCEMA\\Informatica\\Repositorio_Informatica\\Practicas')
print(os.getcwd()) #where now
print(os.listdir())

os.mkdir('NewDir') #create o make
print(os.listdir())

os.rename('NewDir','NewDir2') #rename
print(os.listdir())

os.rmdir('NewDir2') #remove
print(os.listdir())

#EXTRA:
# Para no volver a escribir toda la ruta, si quiero seguir metiendome en carpetas lo que puedo hacer es, suponiendo que me encuentro
# en la carpeta Fundamentos comenzar con un punto: .Fundamentos\Teoricas\tp1.p1
#Para subir de jerarquiza es decir ir hacia a tras se usan dos puntos ..\Estadistica

#Desafio III Abrí el archivo bio.txt y escribí una mini biografía de presentación. 
#recordemos que miarch se puede nombrar como quiera
with open(r"..\Teoricas\Clase 2\bio.txt","w") as bokita:
    bokita.write("Soy Agustin Brogliatti, me gusta hacer renders 3D\ny el rock progresivo :) ")

text = open(r"..\Teoricas\Clase 2\bio.txt","r")

print(text.read())  #lee todo el texto y lo imprimie
print(text.readline()) #lee la primer linea
print(text.readlines()) #lee todas las lineas y las coloca en una lista
#IMPORTANTE: Si ya utilice read el cursor queda clavado al final del techo y no vuelve al inicio por lo que 
#read line o readlines no vana funcionar porque el texto ya fue leido.


text.close()
texto.close()

# Desafio IV Descargá el archivo manipulacion_archivos.txt y creá un programa que lea su contenido y lo imprima en pantalla 
# el resultado de la búsqueda de la expresión -(.*)-

with open(r"C:\Users\agust\Desktop\UCEMA\Informatica\UCEMA_Fundamentos_de_informatica\Python_intro\manipulacion_archivos.txt", "r") as miarch:
    miarch = miarch.read()
    print(miarch)
    print(re.search("-(.*)-", miarch).group(1))


from pathlib import Path

#Cual es el home de nuestro OS
home = str(Path.home())
print(home)

#os.path.join nos genera automaticamente, osea nos escribe las rutas en el formato de nuestro SO, nos facilita el problema 
#Ademas que usando esta funcion hace que sea universal dependiendo donde la ejecutes.
ruta_relativa = os.path.join("UCEMA", "Informatica", "Practicas", "Practica 1")
print(ruta_relativa)

#Poniendo home al principio nos ahorra el C:\Users..., arranca directo de ahi
ruta_absoluta = os.path.join(home, "Desktop", "UCEMA", "Estadistica")
print(ruta_absoluta)

#Para saber si esta ruta existe, porque podriamos estar escribiendo algo que no va a funcionar, ya que la funcion join reescribe 
#segun tu SO pero no verifica que esta ruta exista
print(os.path.exists(ruta_absoluta))
print(os.path.exists(os.path.join(home, "Desktop", "ITBA", "Estadistica")))

print(os.getcwd()) 
os.chdir(r".\Practica 1") #Como antes estaba parado en practicas ahora avanzo una carpeta mas
print(os.getcwd()) 
os.chdir(r"..\Practica 2") #Back, tiene que ser una paralela a mi carpeta
print(os.getcwd()) 


import glob
print(glob.glob("*")) #Es como os.list pero mucho mejor porque le puedo colocar un filtro de busqueda
print(glob.glob("*.py"))


