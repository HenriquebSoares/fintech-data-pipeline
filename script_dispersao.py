import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_dispersao.csv')

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df, x='altura_cm', y='peso_kg', hue='sexo', palette='Set2'
)
plt.title('Dispersão: Altura vs Peso por Sexo')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.tight_layout()
plt.show()