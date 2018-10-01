import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def limpiar(a):
	return a.replace('\'','').replace(',','').replace('+','')
	

df = pd.read_csv(r'D:\\Empresa\\Python Software\\Sonda Veeder\\Older\\file.txt', sep=' ', index_col  = False)
df['Sonda'] = df['Sonda'].replace(['Inconsistencia'], np.nan)
df = df.dropna()
df = df.drop(['Sonda','Anho','Fe','Mes','Dia'], 1)
df['Diferencia'] = df.index
Dif = df['Diferencia'].tolist()
Aka = [0]
for u in range(len(df)-1):
		Aka.append(Dif[u+1]-Dif[u])
df['Diferencia'] = Aka

Agua = df['mmAgua'].tolist()
Fuel = df['mmFuel'].tolist()
Temp = df['Temp'].tolist()
i = 0

Agua = pd.Series([limpiar(l) for l in Agua]).astype('float')
Fuel = pd.Series([limpiar(l) for l in Fuel]).astype('float')
Temp = pd.Series([limpiar(l) for l in Temp]).astype('float')
print(Agua[0:10])
print(Fuel[0:10])
print(Temp[0:10])