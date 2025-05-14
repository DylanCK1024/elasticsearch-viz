import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV del dataset de películas (suponiendo que está en la misma carpeta que el script)
df = pd.read_csv('movies.csv')

# Verificar las primeras filas del dataset para conocer su estructura
print(df.head())

# Filtramos y limpiamos las columnas necesarias
df_filtered = df[['budget', 'revenue', 'vote_average', 'title']].dropna()

# Graficar la relación entre presupuesto, ingresos y promedio de votos
plt.figure(figsize=(12, 6))

# Graficamos presupuesto vs. ingresos
plt.scatter(df_filtered['budget'], df_filtered['revenue'], c=df_filtered['vote_average'], cmap='viridis', alpha=0.6)
plt.title('Relación entre Presupuesto y Ingresos de Películas')
plt.xlabel('Presupuesto (USD)')
plt.ylabel('Ingresos (USD)')
plt.colorbar(label='Promedio de Votos')

# Guardar la imagen como archivo PNG
plt.savefig('grafica_peliculas.png')

# Crear un archivo HTML para mostrar la imagen en GitHub Pages
with open("index.html", "w") as f:
    f.write(f"""
    <html>
      <head><title>Gráfica de Películas</title></head>
      <body>
        <h1>Relación entre Presupuesto, Ingresos y Promedio de Votos de Películas</h1>
        <img src="grafica_peliculas.png" alt="Relación entre Presupuesto e Ingresos de Películas">
      </body>
    </html>
    """)
