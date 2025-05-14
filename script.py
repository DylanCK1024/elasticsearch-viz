from elasticsearch import Elasticsearch
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el CSV
df = pd.read_csv("movies.csv")

# Conectarse al Elasticsearch del contenedor (en Actions estará en localhost:9200)
es = Elasticsearch("http://localhost:9200")

# Crear el índice si no existe
index_name = "movies"
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)

# Indexar documentos
for _, row in df.iterrows():
    doc = row.to_dict()
    es.index(index=index_name, document=doc)

# Visualizar: ejemplo con promedio de votos por idioma original
summary = df.groupby("original_language")["vote_average"].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=summary.values, y=summary.index)
plt.xlabel("Promedio de Voto")
plt.ylabel("Idioma Original")
plt.title("Top 10 idiomas con mayor promedio de voto")
plt.tight_layout()
plt.savefig("grafica.png")
