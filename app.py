import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("Iniciando o processamento dos dados da Fintech...")


    df = pd.read_csv('transacoes.csv', encoding='latin1')
    
    df['valor'] = df.groupby('estado_cliente')['valor'].transform(lambda x: x.fillna(x.median()))
    
    df['plataforma'] = 'Mobile'


    df['data_transacao'] = pd.to_datetime(df['data_transacao'])
    
    df['data_transacao'] = df['data_transacao'].dt.tz_localize('America/Sao_Paulo')
    
    df['dia_semana'] = df['data_transacao'].dt.day_name()
    df['mes'] = df['data_transacao'].dt.month
    
    df = df.drop_duplicates(keep='first')


    filtro_bitwise = (
        (df['mes'] == 9) & 
        (df['estado_cliente'].isin(['SP', 'RJ'])) & 
        (df['valor'] > 5000.0)
    )
    df_filtrado_setembro = df[filtro_bitwise]
    print(f"\nQtd de transações filtradas (Setembro, SP/RJ, >R$5k): {len(df_filtrado_setembro)}")


    risco_dict = {
        'C100': 'Baixo', 
        'C101': 'Alto', 
        'C102': 'Medio', 
        'C103': 'Baixo', 
        'C104': 'Alto'
    }
    
    df['nivel_risco'] = df['id_cliente'].map(risco_dict)
    
    tabela_dinamica = pd.pivot_table(
        df, 
        values='valor', 
        index='mes', 
        columns='nivel_risco', 
        aggfunc='sum', 
        margins=True,
        margins_name='Total'
    )
    print("\nTabela Dinâmica (Soma de Valores por Mês e Risco):")
    print(tabela_dinamica)

    media_estado = df.groupby('estado_cliente')['valor'].transform('mean')
    std_estado = df.groupby('estado_cliente')['valor'].transform('std')
    
    df['z_score'] = (df['valor'] - media_estado) / std_estado
    df_anomalias = df[df['z_score'] > 2.5]
    print(f"\nDetectadas {len(df_anomalias)} possíveis anomalias (Z-Score > 2.5).")

    df_diario = df.groupby(df['data_transacao'].dt.date)['valor'].sum().reset_index()
    
    df_diario['media_movel_7d'] = df_diario['valor'].rolling(window=7).mean()

    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(df_diario['data_transacao'], df_diario['valor'], label='Transações Diárias (Total)', color='#1f77b4', marker='o', alpha=0.7)
    ax.plot(df_diario['data_transacao'], df_diario['media_movel_7d'], label='Média Móvel (7 Dias)', color='#ff7f0e', linewidth=2.5)
    
    ax.set_ylim(bottom=0)
    
    ax.set_title('Desempenho Diário de Transações e Tendência (Média Móvel)', fontsize=14, fontweight='bold')
    ax.set_xlabel('Data', fontsize=12)
    ax.set_ylabel('Valor Total (R$)', fontsize=12)
    
    ax.legend(loc='upper right')
    ax.grid(True, linestyle='--', alpha=0.6)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    fig.savefig('relatorio_visual.png', dpi=300)
    print("\nGráfico 'relatorio_visual.png' gerado com sucesso!")
    
    plt.show()

if __name__ == "__main__":
    main()