#Importar módulos y bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style
import math
from csv import reader
from importlib import reload
from dateutil import parser

reload(plt)



#Leer datos
df = pd.read_csv('Dat2.csv') #si no se lee a través de panda hace líneas rectas ^^

#Para obtener y cambiar el formato de fecha
with open('Dat2.csv', 'r') as f:
	data = list(reader(f))
time = [parser.parse(i[0]) for i in data[1::]]

#Asignar valores a las variables que definen las coordenadas en la gráfica
#X_p = time
X_p = [i[2] for i in data[1::]]
GraphA = df[['Ver']]
GraphB = df[['VerT']]


#Dibujar gráfica y poner etiquetas
plt.plot(X_p, GraphA, 'r-', label='Vertical intensity')
plt.plot(X_p, GraphB, 'b-', label='Theoretical intensity')

plt.legend()
#plt.title('Comparation calculated vertical magnetic field intensity vs teorical one')
#plt.xlabel('Latitude ISS when data is collected')

# =============================================================================
# plt.xticks([1, 20, 40, 60, 80, 100, 120, 140, 160])
# =============================================================================
plt.xticks(rotation=90)
#plt.ylabel('Vertical magnetic field intensity')
plt.show()