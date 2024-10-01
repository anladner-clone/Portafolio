import pandas as pd

# Leer el archivo Excel
df = pd.read_excel('ruta_del_archivo.xlsx')

# Mostrar las primeras filas para verificar los datos
print(df.head())

import matplotlib.pyplot as plt

# Contar cuántos compraron offline y online
canal_compras = df['Canal_de_venta'].value_counts()

# Crear el gráfico de barras
canal_compras.plot(kind='bar', color=['blue', 'orange'])
plt.title('Cantidad de Compras Offline vs Online')
plt.xlabel('Canal de Venta')
plt.ylabel('Cantidad de Personas')
plt.show()

# Agrupar por cliente y sumar el importe total de las compras
clientes_top = df.groupby('ID_Cliente')['Importe_Coste_total'].sum()

# Ordenar los clientes de mayor a menor
clientes_top = clientes_top.sort_values(ascending=False).head(10)  # Los 10 que más compraron

# Crear el gráfico de barras
clientes_top.plot(kind='bar', color='green')
plt.title('Top 10 Clientes que más Compraron')
plt.xlabel('ID del Cliente')
plt.ylabel('Total Gastado')
plt.show()