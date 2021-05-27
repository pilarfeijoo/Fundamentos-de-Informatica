import pandas as pd
import seaborn as sns
import scipy.stats as ss

df = pd.read_csv("/Users/pilarfeijoo/Desktop/fundamentos de informatica/personas_2011.csv", sep=";")
print(df)


print(df.head()) #imprime una parte
print(df.info())
#print(df.tail())
#print(len(df))
print(df.describe()) 
print(df['categoria_conicet_id'])
#print(df.loc[2, 'categoria_conicet_descripcion'])
#print(df.['categoria_conicet_descripcion'].tolist())
print(df.groupby("seniority_level").count().persona_id)


import pandas as pd

#Series (1-dimensional) Las series pueden contener cualquier tipo de datos (enteros, cadenas, números de punto flotante, etc.). Y se pueden crear del siguiente modo:
una_serie = pd.Series(['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], dtype='string')
print(una_serie)

# DataFrames (2-dimensional)
# Un DataFrame es una estructura tabular bidimensional de datos tabulares, potencialmente heterogéneos, con ejes etiquetados (filas y columnas). Las operaciones aritméticas se alinean en las etiquetas de fila y columna. Se puede considerar como un contenedor similar a un dict para objetos Serie.En un DataFrame se almacenan realmente en la memoria como una colección de Series. Podemos crear un DataFrame del sigueinte modo:
paises_latam = pd.DataFrame(data ={"Pais": ['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], "Lengua oficial primaria": ['Español', 'Español', 'Español', 'Español', 'Portugues', 'Español']}, index = [1,2,3,4,5,6])
print(paises_latam)

# DataFrame a partir de un diccionario, claves=columnas y los valores=filas:
#será DataFrame(data=diccionario, index=filas, columns=columnas, dtype=tipos)
datos = {"Pais": ['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], "Idioma oficial": ['Español', 'Español', 'Español', 'Español', 'Portugues', 'Español']}
df = pd.DataFrame(datos)
print(df)


# Desafío I: Estos métodos aceptan otros parámetros que merecen la pena ser explorados. Averiguá para qué sirven los parámetro sep, index_col, nrows y header

df = pd.read_csv(, sep=";", nrows=5, header=2, index_col=3)
#nrows: Devuelve primeras 5 filas

#header: Devuelve de la fila 2 hacia abajo

#index_col: Devuelve de la columna 3 hacia la derecha, admite str o int.