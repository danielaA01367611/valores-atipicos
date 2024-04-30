import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_excel('gastos_costos_20_23.xlsx')
#print(df.head())

valores_nulos=df.isnull().sum()
#print(valores_nulos)

#LIMPIEZA DE NULOS
df['FOLIO']=df['FOLIO'].fillna('DESCONOCIDO')

df['GASTO']=df['GASTO'].fillna('GASTO NO RECONOCIDO')

df['TC'] =df['TC'].ffill()

df['IMPORTE'] =df['IMPORTE'].fillna(round(df['IMPORTE'].mean(),1))

df['IVA'] =df['IVA'].fillna(0)

df['TIPO']=df['TIPO'].fillna('DESCONOCIDO')

df['POLIZA']=df['POLIZA'].fillna('FALTANTE')
valores_nulos=df.isnull().sum()
#print(valores_nulos)

#print(df.info())

#PRIMERA COLUMNA: IMPORTE

#histograma inicial
fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["IMPORTE"], color='red', rwidth=0.50)
plt.title('Histograma de Importe')
plt.xlabel('Importe')
plt.ylabel('Frecuencia')
#plt.show()

#boxplot inicial
fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["IMPORTE"]) 
plt.title("Outliers de IMPORTE")
#plt.show()

#MÉTODO ENCONTRANDO CUARTILES.
y=df["IMPORTE"]
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

#Realizamos diagrama de caja o bigotes limpio
fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr["IMPORTE"]) 
plt.title("Importe sin outliers (metodo cuartiles)")
#plt.show()

#Realizamos histograma limpio
fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["IMPORTE"], color='blue', rwidth=0.50)
plt.title('Histograma de Importe sin outliers (metodo cuartiles)')
plt.xlabel('Importe')
plt.ylabel('Frecuencia')
#plt.show()

#data_clean_iqr["IMPORTE"].to_csv('IMPORTE_sin_outliers.csv')

#MÉTODO DESVIACIÓN ESTANDAR
y=df["IMPORTE"]
Limite_Superior_dev_std= y.mean() + 3 * y.std()
Limite_Inferior_dev_std= y.mean() - 3 * y.std()
#print("Limite superior permitido usando desviación estandar", Limite_Superior_dev_std)
#print("Limite inferior permitido usando desviación estandar", Limite_Inferior_dev_std)

#Obtenemos datos limpios
data_clean_dev_std= df[(y<=Limite_Superior_dev_std)&(y>=Limite_Inferior_dev_std)]
#print(data_clean_dev_std)

#Realizamos diagrama de caja o bigotes limpio
fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr["IMPORTE"]) 
plt.title("Importe sin outliers (metodo std)")
#plt.show()

#Obtenemos histograma limpio
fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["IMPORTE"], color='blue', rwidth=0.50)
plt.title('Histograma de IMPORTE sin outliers con std')
plt.xlabel('IMPORTE')
plt.ylabel('Frecuencia')
#plt.show()

#data_clean_dev_std["IMPORTE"].to_csv('IMPORTE_sin_outliers(std).csv')

#SEGUNDA COLUMNA: IVA

#histograma inicial
fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["IVA"], color='red', rwidth=0.50)
plt.title('Histograma de IVA')
plt.xlabel('IVA')
plt.ylabel('Frecuencia')
#plt.show()

#boxplot inicial
fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["IVA"]) 
plt.title("Outliers de IVA")
#plt.show()

#MÉTODO ENCONTRANDO CUARTILES.
y=df["IVA"]
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

#Realizamos diagrama de caja o bigotes limpio
fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr["IVA"]) 
plt.title("IVA sin outliers (metodo cuartiles)")
#plt.show()

#Realizamos histograma limpio
fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["IVA"], color='blue', rwidth=0.50)
plt.title('Histograma de IVA sin outliers (metodo cuartiles)')
plt.xlabel('IVA')
plt.ylabel('Frecuencia')
#plt.show()

#data_clean_iqr["IVA"].to_csv('IVA_sin_outliers.csv')

#MÉTODO DESVIACIÓN ESTANDAR
y=df["IVA"]
Limite_Superior_dev_std= y.mean() + 3 * y.std()
Limite_Inferior_dev_std= y.mean() - 3 * y.std()
#print("Limite superior permitido usando desviación estandar", Limite_Superior_dev_std)
#print("Limite inferior permitido usando desviación estandar", Limite_Inferior_dev_std)

#Obtenemos datos limpios
data_clean_dev_std= df[(y<=Limite_Superior_dev_std)&(y>=Limite_Inferior_dev_std)]
#print(data_clean_dev_std)

#Realizamos diagrama de caja o bigotes limpio
fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr["IVA"]) 
plt.title("IVA sin outliers (metodo std)")
#plt.show()

#Obtenemos histograma limpio
fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["IVA"], color='blue', rwidth=0.50)
plt.title('Histograma de IVA sin outliers con std')
plt.xlabel('IVA')
plt.ylabel('Frecuencia')
#plt.show()

data_clean_dev_std["IVA"].to_csv('IVA_sin_outliers(std).csv')
