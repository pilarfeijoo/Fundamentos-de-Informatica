#Ejercicio 6
#Escribí un programa que dado dos diccionarios genere dos DataFrame y los una tanto en el eje de las columnas como en el eje de las filas.
import pandas as pd

uno = {1: ["Pilar", "Agustin", "Nicole"], 2: ["Feijoo","Martinez","Perez"]}
dos = {"a": [5, 6, 3], "b": [4,7,6], "c": [9,0,9]}
df1 = pd.DataFrame(uno)
df2 = pd.DataFrame(dos)

columnas =pd.concat([df1,df2],ignore_index=True, sort=False)
print(columnas)
filas= pd.concat([df1, df2], axis=1)
print(filas)