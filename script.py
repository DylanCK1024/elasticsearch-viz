import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# Leer el archivo CSV del dataset de películas
df = pd.read_csv('movies.csv')

# Limpiar y filtrar las columnas necesarias
df_filtered = df[['budget', 'revenue', 'vote_average', 'title', 'genres']].dropna()

# Establecer un estilo visual con Seaborn
sns.set(style="whitegrid")

# Crear una figura para los gráficos
plt.figure(figsize=(15, 10))

# Gráfico de dispersión 3D para visualizar la relación entre presupuesto, ingresos y promedio de votos
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111, projection='3d')

# Ejes del gráfico
ax.scatter(df_filtered['budget'], df_filtered['revenue'], df_filtered['vote_average'], c=df_filtered['vote_average'], cmap='viridis', alpha=0.7)

# Etiquetas y título
ax.set_xlabel('Presupuesto (USD)')
ax.set_ylabel('Ingresos (USD)')
ax.set_zlabel('Promedio de Votos')
ax.set_title('Relación entre Presupuesto, Ingresos y Promedio de Votos')

# Guardar el gráfico 3D como archivo PNG
plt.savefig('grafica_3d.png')

# Crear un histograma para mostrar la distribución del presupuesto y los ingresos
plt.figure(figsize=(12, 6))
plt.hist(df_filtered['budget'], bins=50, alpha=0.6, color='blue', label='Presupuesto')
plt.hist(df_filtered['revenue'], bins=50, alpha=0.6, color='green', label='Ingresos')
plt.title('Distribución de Presupuesto e Ingresos de Películas')
plt.xlabel('Monto (USD)')
plt.ylabel('Frecuencia')
plt.legend()

# Guardar el histograma como archivo PNG
plt.savefig('histograma.png')

# Gráfico de barras para mostrar el promedio de votos por género
# Primero, vamos a dividir los géneros y contar cuántas películas hay por género
df_filtered['genres'] = df_filtered['genres'].apply(lambda x: x.split('|')[0] if isinstance(x, str) else 'Unknown')
vote_by_genre = df_filtered.groupby('genres')['vote_average'].mean().sort_values(ascending=False)

# Crear el gráfico de barras
plt.figure(figsize=(12, 6))
vote_by_genre.plot(kind='bar', color='teal')
plt.title('Promedio de Votos por Género de Películas')
plt.xlabel('Género')
plt.ylabel('Promedio de Votos')
plt.xticks(rotation=90)

# Guardar el gráfico de barras como archivo PNG
plt.savefig('grafica_barras.png')

# Crear un archivo HTML para mostrar todos los gráficos en GitHub Pages
with open("index.html", "w") as f:
    f.write(f"""
    <html>
      <head><title>Gráficas de Películas</title></head>
      <body>
        <h1>Visualización Detallada de Películas</h1>
        <h2>1. Relación entre Presupuesto, Ingresos y Promedio de Votos</h2>
        <img src="grafica_3d.png" alt="Gráfico 3D de Presupuesto vs. Ingresos vs. Promedio de Votos">
        <h2>2. Distribución de Presupuesto e Ingresos</h2>
        <img src="histograma.png" alt="Histograma de Presupuesto e Ingresos">
        <h2>3. Promedio de Votos por Género</h2>
        <img src="grafica_barras.png" alt="Gráfico de Promedio de Votos por Género">
      </body>
    </html>
    """)
