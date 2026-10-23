import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_frequencia.csv')

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='tipo_atendimento', palette='viridis')
plt.title('Frequência por Tipo de Atendimento')
plt.xlabel('Tipo de Atendimento')
plt.ylabel('Contagem')
plt.tight_layout()
plt.show()