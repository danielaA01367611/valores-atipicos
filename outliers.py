import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt

#print('hello outliers')
df= pd.read_csv('ventas_totales_sinnulos.csv', index_col=0)
#print(df.head())

valores_nulos=df.isnull().sum()
#print(valores_nulos)

#print(df.info())

#ventas_precios_corrientes

fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["ventas_precios_corrientes"], color='red', rwidth=0.50)
plt.title('Histograma de ventas_precios_corrientes')
plt.xlabel('ventas_precios_corrientes')
plt.ylabel('Frecuencia')
#plt.show()

fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["ventas_precios_corrientes"]) 
plt.title("Outliers de ventas_precios_corriente")
#plt.show()

#Método aplicando Cuartiles. Encuentro cuartiles 0.25 y 0.75
y=df["ventas_precios_corrientes"]
#print(y)

percentile25=y.quantile(0.25) #Q1
#print(percentile25)
percentile75=y.quantile(0.75) #Q3
#print(percentile75)
iqr= percentile75 - percentile25
#print(iqr)

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr
#print("Limite superior permitido", Limite_Superior_iqr)
#print("Limite inferior permitido", Limite_Inferior_iqr)

#Obtenemos datos limpios
data_clean_iqr= df[(y<=Limite_Superior_iqr)&(y>=Limite_Inferior_iqr)]
#print(data_clean_iqr)

#Realizamos diagrama de caja o bigote
fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr["ventas_precios_corrientes"]) 
plt.title("No Outliers de ventas_precios_corrientes")
#plt.show()

fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["ventas_precios_corrientes"], color='blue', rwidth=0.50)
plt.title('Histograma de ventas_precios_corriente sin outliers')
plt.xlabel('ventas_precios_corriente')
plt.ylabel('Frecuencia')
#plt.show()

#data_clean_iqr["ventas_precios_corrientes"].to_csv('ventas_precios_corrientes.csv')

#MÉTODO DESVIACIÓN ESTANDAR
y=df["ventas_precios_corrientes"]
Limite_Superior_dev_std= y.mean()+3*y.std()
Limite_Inferior_dev_std=y.mean()-3*y.std()
#print("Limite superior permitido usando desviación estandar", Limite_Superior_dev_std)
#print("Limite inferior permitido usando desviación estandar", Limite_Inferior_dev_std)

#Obtenemos datos limpios
data_clean_dev_std= df[(y<=Limite_Superior_dev_std)&(y>=Limite_Inferior_dev_std)]
#print(data_clean_dev_std)

fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["ventas_precios_corrientes"], color='blue', rwidth=0.50)
plt.title('Histograma de ventas_precios_corriente sin outliers con std')
plt.xlabel('ventas_precios_corriente')
plt.ylabel('Frecuencia')
plt.show()

data_clean_dev_std["ventas_precios_corrientes"].to_csv('ventas_precios_corrientes_sin_outliers(std).csv')