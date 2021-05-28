#Escribí un programa que sume, reste, multiplique y divida dos series de números de Pandas.

#Series de muestra:

#[3, 7, 12, 15, 21], [1, 4, 10, 14, 19]


import pandas as pd
import seaborn as sns
import scipy.stats as ss

serie1 = [3, 7, 12, 15, 21]
serie2 = [1, 4, 10, 14, 19]

df = pd.Series(serie1)
df2 = pd.Series(serie2)

#va sumando por las posiciones
suma = (df+df2)
print(suma)

resta = (df-df2)
print(resta)

multiplique = (df*df2)
print(multiplique)

division = (df/df2)
print(division)