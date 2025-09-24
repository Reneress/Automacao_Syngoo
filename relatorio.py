import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns


def executar_relatorio():
    # Caminho do arquivo Excel de origem
    arquivo_excel = "arquivos/notas.xlsx"

    # Caminho de destino para salvar o Excel resumido
    arquivo_saida = "Resumo_notas/resumo_agentes.xlsx"

    # 1. Lê o arquivo Excel
    df = pd.read_excel(arquivo_excel)

    # Converte coluna Data para datetime
    df['Data'] = pd.to_datetime(df['Data'])

    # 2. Separa a coluna "Resposta" em duas: "Agente" e "Nota"
    df[['Agente', 'Nota']] = df['Resposta'].str.split(' - ', expand=True)
    df['Nota'] = df['Nota'].astype(float)

    # 3. Cria resumo por agente
    resumo = df.groupby('Agente').agg(
        Numero_Atendimentos=('Nota', 'count'),
        Media_Notas=('Nota', 'mean'),
        Maior_Nota=('Nota', 'max'),
        Menor_Nota=('Nota', 'min')
    ).reset_index()

    # 4. Adiciona Data e Nome do atendimento com maior e menor nota
    def atendimento_maior(row):
        linha = df[(df['Agente'] == row['Agente']) & (df['Nota'] == row['Maior_Nota'])].iloc[0]
        return pd.Series([linha['Data'], linha['Nome']])

    def atendimento_menor(row):
        linha = df[(df['Agente'] == row['Agente']) & (df['Nota'] == row['Menor_Nota'])].iloc[0]
        return pd.Series([linha['Data'], linha['Nome']])

    resumo[['Data_Maior_Nota', 'Nome_Maior_Nota']] = resumo.apply(atendimento_maior, axis=1)
    resumo[['Data_Menor_Nota', 'Nome_Menor_Nota']] = resumo.apply(atendimento_menor, axis=1)

    # 5. Salva o resumo em Excel
    resumo.to_excel(arquivo_saida, index=False)
    print(f"Arquivo resumo salvo em: {arquivo_saida}")

    import matplotlib.pyplot as plt
    import matplotlib.ticker as mtick
    sns.set_style('whitegrid')
    # 6. Plota gráfico de barras horizontais da média das notas
    media_total = resumo.set_index('Agente')['Media_Notas'].sort_values(ascending=False)

    plt.figure(figsize=(12, 8))
    # plt.style.use('seaborn-whitegrid')  # estilo mais limpo e moderno

    # Gradiente de tons de verde
    cores = plt.cm.Greens((media_total.values - media_total.values.min()) /
                        (media_total.values.max() - media_total.values.min()))

    bars = plt.barh(media_total.index, media_total.values, color=cores, edgecolor='black')

    # Adiciona valores nas barras
    for bar in bars:
        width = bar.get_width()
        plt.text(width + 0.05, bar.get_y() + bar.get_height()/2,
                f'{width:.2f}', va='center', fontsize=12, fontweight='bold', color='darkgreen')

    # Configurações estéticas
    plt.xlabel('Nota Média', fontsize=14, fontweight='bold')
    plt.ylabel('Agente', fontsize=14, fontweight='bold')
    plt.title('Média de Notas por Agente (Maior → Menor)', fontsize=16, fontweight='bold', pad=20)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.gca().invert_yaxis()  # maior valor no topo

    # Adiciona linhas de grade horizontais leves
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()


# executar_relatorio()