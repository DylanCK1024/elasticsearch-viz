from elasticsearch import Elasticsearch
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo CSV
df = pd.read_csv("movies.csv")

# Convertir columnas con listas o diccionarios a cadenas de texto
columns_to_convert = [
    'genres', 'keywords', 'cast', 'crew',
    'production_companies', 'production_countries', 'spoken_languages'
]

for col in columns_to_convert:
    if col in df.columns:
        df[col] = df[col].astype(str)

# Reemplazar valores nulos con cadenas vacías
df.fillna("", inplace=True)

# Conectar a Elasticsearch (localhost:9200, asegúrate de que esté corriendo)
es = Elasticsearch("http://localhost:9200")

# Nombre del índice
index_name = "movies"

# Crear el índice si no existe
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)

# Indexar documentos en Elasticsearch
for _, row in df.iterrows():
    try:
        doc = row.to_dict()
        es.index(index=index_name, document=doc)
    except Exception as e:
        print(f"Error al indexar documento: {e}")

# Crear una gráfica: promedio de votación por idioma original (Top 10)
try:
    summary = df.groupby("original_language")["vote_average"].mean().sort_values(ascending=False).head(10)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=summary.values, y=summary.index)
    plt.xlabel("Promedio de Voto")
    plt.ylabel("Idioma Original")
    plt.title("Top 10 idiomas con mayor promedio de voto")
    plt.tight_layout()
    plt.savefig("grafica.png")
except Exception as e:
    print(f"Error al generar la gráfica: {e}")
