from elasticsearch import Elasticsearch
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer CSV
df = pd.read_csv("movies.csv")

# Convertir columnas complejas a texto plano
for col in ['genres', 'keywords', 'cast', 'crew', 'production_companies', 'production_countries', 'spoken_languages']:
    if col in df.columns:
        df[col] = df[col].astype(str)

# Reemplazar NaNs
df = df.fillna("")

# Conectarse a Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Nombre del índice
index_name = "movies"

# Definir un mapping explícito para evitar errores 400
mapping = {
    "mappings": {
        "properties": {
            "title": {"type": "text"},
            "original_language": {"type": "keyword"},
            "vote_average": {"type": "float"},
            "release_date": {"type": "date", "format": "yyyy-MM-dd"},
            "runtime": {"type": "integer"},
            "budget": {"type": "long"},
            "revenue": {"type": "long"}
        }
    }
}

# Crear índice con mapping si no existe
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name, body=mapping)

# Indexar primeros 100 documentos para evitar errores masivos
for _, row in df.head(100).iterrows():
    try:
        doc = row.to_dict()
        es.index(index=index_name, document=doc)
    except Exception as e:
        print(f"Error al indexar documento: {e}")
        print(doc)

# Graficar: promedio de votos por idioma original
summary = df.groupby("original_language")["vote_average"].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=summary.values, y=summary.index)
plt.xlabel("Promedio de Voto")
plt.ylabel("Idioma Original")
plt.title("Top 10 idiomas con mayor promedio de voto")
plt.tight_layout()
plt.savefig("grafica.png
