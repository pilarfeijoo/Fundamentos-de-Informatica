#Ejercicio 2
#Realizá un programa que compare (si son mayores, menores o iguales) los elementos de dos series de números de Pandas.

#Series de muestra:

#[3, 7, 9, 14, 25], [1, 7, 10, 16, 19]

import pandas as pd

serie1 = [3, 7, 9, 14, 25]
serie2 = [1, 7, 10, 16, 19]

df = pd.Series(serie1)
df2 = pd.Series(serie2)

es_mayor = (df>df2)
print(es_mayor)

es_menor = (df<df2)
print(es_menor)

es_igual = (df==df2)
print(es_igual)