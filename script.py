import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame de ejemplo
data = pd.DataFrame({
    'Día': ['Lun', 'Mar', 'Mié', 'Jue', 'Vie'],
    'Visitas': [120, 230, 180, 250, 300]
})

# Crear gráfica
plt.figure(figsize=(8, 5))
plt.bar(data['Día'], data['Visitas'], color='skyblue')
plt.title('Visitas por Día')
plt.xlabel('Día')
plt.ylabel('Visitas')
plt.tight_layout()

# Guardar como imagen
plt.savefig('grafica.png')

# Crear archivo HTML para mostrar la imagen
with open("index.html", "w") as f:
    f.write(f"""
    <html>
      <head><title>Gráfica</title></head>
      <body>
        <h1>Visitas Semanales</h1>
        <img src="grafica.png" alt="Gráfica de visitas">
      </body>
    </html>
    """)
