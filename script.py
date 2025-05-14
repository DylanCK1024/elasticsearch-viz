from elasticsearch import Elasticsearch
import pandas as pd

# Leer el archivo CSV de películas
df = pd.read_csv('movies.csv')

# Conectar a Elasticsearch
es = Elasticsearch("http://localhost:9201")  # Cambiar la URL si usas Elastic Cloud o algún otro servidor

# Crear un índice (si no existe ya)
index_name = "movies"
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)

# Indexar cada documento (película)
for _, row in df.iterrows():
    doc = row.to_dict()
    es.index(index=index_name, document=doc)

print("Datos cargados en Elasticsearch!")
