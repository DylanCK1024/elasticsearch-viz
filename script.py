from elasticsearch import Elasticsearch
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import time

# Conectar a Elasticsearch sin seguridad
es = Elasticsearch("http://localhost:9200")

# Esperar que Elasticsearch esté disponible
for i in range(30):
    try:
        if es.ping():
            print("✅ Elasticsearch está listo.")
            break
    except:
        time.sleep(2)
else:
    raise Exception("❌ No se pudo conectar a Elasticsearch.")

# Crear índice si no existe
index_name = "mi_indice"
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)

# Datos de ejemplo
data = [
    {"nombre": "Producto A", "precio": 100},
    {"nombre": "Producto B", "precio": 150},
    {"nombre": "Producto C", "precio": 200},
]

# Indexar datos
for i, doc in enumerate(data):
    es.index(index=index_name, id=i + 1, document=doc)

# Obtener los documentos
res = es.search(index=index_name, body={"query": {"match_all": {}}})
docs = [hit["_source"] for hit in res["hits"]["hits"]]

# Convertir a DataFrame
df = pd.DataFrame(docs)

# Graficar
plt.figure(figsize=(8, 5))
sns.barplot(x="nombre", y="precio", data=df)
plt.title("Precios de Productos")
plt.xlabel("Producto")
plt.ylabel("Precio")
plt.tight_layout()
plt.savefig("grafica.png")
print("📊 Gráfica guardada como grafica.png")
