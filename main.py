import pandas as pd

# Leer el archivo Excel
df = pd.read_excel('python\Registros.xlsx')

# Contar cuántos compraron offline y online
canal_compras = df['Canal_de_venta'].value_counts()

print(canal_compras)

tipo_de_producto = df['Tipo de producto'].value_counts()

print(tipo_de_producto)

clientes_top = df.groupby(['ID_Cliente','Zona'])['Importe_Coste_total'].sum()
clientes_top = clientes_top.sort_values(ascending=False).head(10)
print(clientes_top)
