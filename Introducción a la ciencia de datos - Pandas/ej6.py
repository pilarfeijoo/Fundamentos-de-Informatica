#Ejercicio 6
#Escribí un programa que muestre un resumen de la información básica de un DataFrame y sus datos.

#Muestra:

datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}

labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


import pandas as pd

df=pd.DataFrame(datos_ejemplo)
print(df.info)
df2 = pd.Series(labels)
print(df2.describe)


