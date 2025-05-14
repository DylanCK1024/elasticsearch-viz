import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("covid.csv")
df_mx = df[(df['location'] == 'Mexico') & (df['date'].str.startswith('2021'))]
df_mx = df_mx[['date', 'new_cases']].fillna(0)
df_mx['date'] = pd.to_datetime(df_mx['date'])
df_mx = df_mx.sort_values('date')

plt.figure(figsize=(12, 6))
plt.plot(df_mx['date'], df_mx['new_cases'], label="Nuevos casos")
plt.title("COVID-19 en México - 2021")
plt.xlabel("Fecha")
plt.ylabel("Casos diarios")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("covid_mexico_2021.png")
