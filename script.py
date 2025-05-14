from elasticsearch import Elasticsearch
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer CSV
df = pd.read_csv("movies.csv")

# Convertir columnas con tipos complejos a texto plano
for col in ['genres', 'keywords', 'cast', 'crew', 'production_companies', 'production_countries', 'spoken_languages']:
    if col in df.columns:
        df[col] = df[col].astype(str)

# Reemplazar NaNs
df = df.fillna("")

# Conectarse a Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Crear índice si no existe
index_name = "movies"
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)

# Indexar documentos
for _, row in df.iterrows():
    try:
        doc = row.to_dict()
        es.index(index=index_name, document=doc)
    except Exception as e:
        print(f"Error al indexar documento: {e}")

# Graficar: promedio de votos por idioma original
summary = df.groupby("original_language")["vote_average"].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=summary.values, y=summary.index)
plt.xlabel("Promedio de Voto")
plt.ylabel("Idioma Original")
plt.title("Top 10 idiomas con mayor promedio de voto")
plt.tight_layout()
plt.savefig("grafica.png")
