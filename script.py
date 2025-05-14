from elasticsearch import Elasticsearch
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Conectar a Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Verificar la conexión
if es.ping():
    print("Conectado a Elasticsearch")
else:
    print("No se pudo conectar a Elasticsearch")

# Nombre del índice
index_name = 'tu_indice'

# Buscar los datos en Elasticsearch
response = es.search(index=index_name, body={
    "query": {
        "match_all": {}
    },
    "size": 10000  # Ajusta el tamaño si es necesario
})

# Extraer los datos de la respuesta
hits = response['hits']['hits']

# Convertir los resultados a un DataFrame de pandas
data = pd.DataFrame([hit['_source'] for hit in hits])

# Mostrar las primeras filas de los datos para asegurarse de que se han recuperado correctamente
print(data.head())

# Crear una gráfica (ajustar según tus datos)
plt.figure(figsize=(10, 6))
sns.barplot(x=data.columns[0], y=data.columns[1], data=data)  # Ajusta las columnas para la gráfica
plt.title('Gráfica de Datos de Elasticsearch')
plt.xlabel(data.columns[0])
plt.ylabel(data.columns[1])
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
