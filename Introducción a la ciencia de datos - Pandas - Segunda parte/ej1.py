#Ejercicio 1
#Escribí un programa que dado un diccionario cuyos valores sean listas de números cree un DataFrame y luego seleccione e imprima las filas del DataFrame basado en un valor de una columna.

#Diccionario de muestra: {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]}, y el valor es 4 en la columna 1.

import pandas as pd
dic = {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]}
df = pd.DataFrame(dic)
print(df)

print(df.loc[df[1]==4])
