#Ejercicio 3
#Escribí un programa para convertir un diccionario a una serie de Pandas.

#Diccionario de muestra:

#dict1 = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}

import pandas as pd 

dict1 = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}

serie = pd.Series(dict1)

print(serie)