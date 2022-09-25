# APARTADO 1

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure 

df = pd.read_csv('finanzas2020.csv', sep = '\t')

try:
    gastos = df[df<0].sum()
    print(gastos[gastos == gastos.min()])
except Exception as e:
    print(e)

df['Enero'] = pd.to_numeric(df.Enero, errors='coerce')
df['Febrero'] = pd.to_numeric(df.Febrero, errors='coerce')
df['Marzo'] = pd.to_numeric(df.Marzo, errors='coerce')
df['Abril'] = pd.to_numeric(df.Abril, errors='coerce')
df['Mayo'] = pd.to_numeric(df.Mayo, errors='coerce')
df['Junio'] = pd.to_numeric(df.Junio, errors='coerce')
df['Julio'] = pd.to_numeric(df.Julio, errors='coerce')
df['Agosto'] = pd.to_numeric(df.Agosto, errors='coerce')
df['Septiembre'] = pd.to_numeric(df.Septiembre, errors='coerce')
df['Octubre'] = pd.to_numeric(df.Octubre, errors='coerce')
df['Noviembre'] = pd.to_numeric(df.Noviembre, errors='coerce')
df['Diciembre'] = pd.to_numeric(df.Diciembre, errors='coerce')

try:
    gastos = df[df<0].sum()
    print(gastos[gastos == gastos.min()])
except Exception as e:
    print(e)

try:
    ing = df[df>0].sum()
    print(ing[ing == ing.max()])
except Exception as e:
    print(e)

try:
    print(df[df<0].mean().mean())
except Exception as e:
    print(e)

print(gastos.sum())

print(ing.sum())

x = df.columns
y = ing
figure(figsize=(15, 15), dpi=80)
plt.plot(x, y)  
plt.xlabel("Mes")  
plt.ylabel("Ingresos")  
plt.title("Ingresos a lo largo del año")  
plt.show()
plt.savefig("Ingresos_año.jpg")


# APARTADO 2

try:
    df = pd.read_csv('finanzas2020.csv', sep = '\t')
except OSError as e:
    print('No existe el fichero.')

assert len(df.columns) == 12, 'El archivo no tiene 12 columnas.'

for i in df.columns:
    assert not(df[i].empty) , f'La columna {i} no tiene contenido.'

for i in df.columns:
    try:
        assert type(df[i]) == int
    except Exception as e:
        df[i] = pd.to_numeric(df[i], errors='coerce')
