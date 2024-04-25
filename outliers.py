import pandas as pd
import numpy as np
import matplotlib as plt

#print('hello outliers')
df= pd.read_csv('ventas_totales_sinnulos.csv', index_col=0)
#print(df.head())

valores_nulos=df.isnull().sum()
#print(valores_nulos)

#fig = plt.figure(figsize =(7, 3))
#plt.hist(x=df["ventas_precios_corrientes"], color='blue', rwidth=0.50)
#plt.title('Histograma de ventas_precios_corrientes')
#plt.xlabel('ventas_precios_corrientes')
#plt.ylabel('Frecuencia')
#plt.show()

#fig = plt.figure(figsize =(5, 3))
#plt.boxplot(df["ventas_precios_corrientes"]) 
#plt.title("Outliers de ventas_precios_corriente")
#plt.show()

y=df["ventas_precios_corrientes"]

percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
iqr= percentile75 - percentile25
#print(percentile25)
#print(iqr)
#print(percentile75)

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr
print("Limite superior permitido usando cuartiles", Limite_Superior_iqr)
print("Limite inferior permitido usando cuartiles", Limite_Inferior_iqr)

#obtenemos los datos limpios
data_clean_iqr= df[(y<=Limite_Superior_iqr)&(y>=Limite_Inferior_iqr)]
#print(data_clean_iqr)

#fig = plt.figure(figsize =(5, 3))
#plt.boxplot(data_clean_iqr["ventas_precios_corrientes"]) 
#plt.title("Outliers de ventas_precios_corrientes")
#plt.show()

#fig = plt.figure(figsize =(7, 3))
#plt.hist(x=df["ventas_precios_corrientes"], color='blue', rwidth=0.50)
#plt.title('Histograma de ventas_precios_corrientes sin outliers')
#plt.xlabel('ventas_precios_corrientes')
#plt.ylabel('Frecuencia')
#plt.show()

#data_clean_iqr["ventas_precios_corrientes"].to_csv('ventas_precios_corrientes.csv')


y=df["ventas_precios_corrientes"]
Limite_Superior= y.mean() + 3*y.std()
Limite_Inferior= y.mean() - 3*y.std()
print("Limite superior permitido usando std", Limite_Superior)
print("Limite inferior permitido usando std", Limite_Inferior)

data_clean_iqr= df[(y<=Limite_Superior_iqr)&(y>=Limite_Inferior_iqr)]
print(data_clean_iqr)

#histograma

#boxplot

#fue mas eficiente el uso de cuartiles para eliminar los valores atipicos

