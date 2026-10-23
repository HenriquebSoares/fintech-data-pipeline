import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dados_heatmap.csv')
pivot_df = df.pivot(
    index='dia_semana', columns='horario', values='movimento_clientes'
)

dias_ordem = [
    'Segunda',
    'Terça',
    'Quarta',
    'Quinta',
    'Sexta',
    'Sábado',
    'Domingo',
]
pivot_df = pivot_df.reindex(dias_ordem)

plt.figure(figsize=(10, 6))
sns.heatmap(pivot_df, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Heatmap: Movimento de Clientes por Dia e Horário')
plt.xlabel('Horário')
plt.ylabel('Dia da Semana')
plt.tight_layout()
plt.show()