import pandas as pd
import seaborn as sns
import scipy.stats as ss

df = pd.read_csv("/Users/pilarfeijoo/Desktop/fundamentos de informatica/personas_2011.csv", sep=";")
print(df)


print(df.head())
print(df.info())
#print(df.tail())
#print(len(df))
print(df.describe())
print(df['categoria_conicet_id'])
#print(df.loc[2, 'categoria_conicet_descripcion'])
#print(df.['categoria_conicet_descripcion'].tolist())



