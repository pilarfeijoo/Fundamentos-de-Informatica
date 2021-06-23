import pandas as pd
df = pd.read_csv("/Users/pilarfeijoo/Desktop/fundamentos de informatica/Fundamentos-de-Informatica/tablas de datos/personas_2011.csv",sep = ";")
print(df)
print(df.head()) # primeras 5 filas
print(df.describe()) #datos estadisticos (mean, count, max, min etc.) se usa para el analisis de los datos.
print(df.tail()) #las ultimas 5 filas
print(len(df)) #cantidad de filas 
print(df.info()) # datos no nulos se encuentran  y tipos de datos 
#Podemos acceder a los datos de cada columna haciendo
# df['nombre de la columna']:
print(df['persona_id']) 
print(df.loc[2, 'persona_id'])  
print(df.loc[2,"edad"]) 


#Desafío IV: 
# Extrae la columna seniority_level y contá cuántas personas tenían expertice nivel B, C y D
print(df.groupby("seniority_level")) 
print(df.groupby("seniority_level").count()) 

print(df.groupby("seniority_level")[["persona_id"]].count()) 
# B = 6674, C = 13645 y D = 5774
print(df['edad'] * 2) # numero entero, multiplica la edad x2
print(df['edad'] + 2) # numero entero, se le suma a la edad 2
print(df['edad'] > 2) # booleano, true>2 false<2, -1 false
print(df[df['edad'] > 35 ]) # +de35 años.


#Desafío V: 
#Contá cuántas personas de 30 años ingresaron al ministerio en 2011 
#¿Cuántas formas de hacer este cálculo se te ocurren?
print(df[df["edad"]== 30]) 

print(df['maximo_grado_academico_id'].value_counts())