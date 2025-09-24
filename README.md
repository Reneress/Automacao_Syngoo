# Automação de Relatórios de Notas do Syngoo Talk

Este projeto tem como finalidade **automatizar o processo de obtenção, organização e análise de relatórios de desempenho dos atendentes no Syngoo Talk**.
A solução reduz o tempo gasto em tarefas manuais e gera **informações consolidadas e visualmente claras** para apoiar a tomada de decisões.

---

## 📌 Objetivo

* Eliminar o processo manual de geração e download de relatórios no Syngoo Talk.
* Garantir padronização e confiabilidade na análise das notas dos atendentes.
* Fornecer **relatórios resumidos e gráficos** de fácil interpretação.

---

## 🔄 Etapas do Processo Automatizado

### 1. Extração Automática (`auto.py`)

* Acessa o Syngoo Talk via **Selenium**.
* Realiza o login com credenciais de administrador.
* Gera o relatório de **NOTA\_AGENTE**.
* Faz o download do arquivo em formato **.xlsx**.

➡️ **Resultado**: relatório bruto obtido automaticamente.

---

### 2. Importação e Organização (`import_.py`)

* Localiza o arquivo **ZIP** baixado.
* Extrai o conteúdo para a pasta `/arquivos`.
* Renomeia o arquivo principal para **notas.xlsx**.

➡️ **Resultado**: arquivo padronizado, pronto para análise.

---

### 3. Processamento e Análise (`relatorio.py`)

* Lê o arquivo **notas.xlsx** com **Pandas**.
* Separa as informações de **Agente** e **Nota**.
* Calcula estatísticas por agente:

  * Total de atendimentos
  * Média das notas
  * Maior e menor nota (com data e cliente associados)
* Gera o arquivo consolidado **resumo\_agentes.xlsx**.
* Cria um **gráfico comparativo** de desempenho dos atendentes.

➡️ **Resultado**: relatório consolidado + visualização gráfica.

---

### 4. Interface Gráfica (`controler.py`)

* Criada com **Tkinter + ttkbootstrap**.
* Disponibiliza botões para:

  * Executar apenas a extração
  * Executar apenas a importação
  * Executar apenas a análise
  * Executar importação + análise
  * Executar todo o processo completo
* Exibe mensagens de sucesso ou erro para o usuário.

➡️ **Resultado**: uso simplificado, sem necessidade de mexer no código.

---

## 🛠️ Tecnologias Utilizadas

* **Selenium** → Automação de navegação no Syngoo Talk.
* **Pandas, Matplotlib, Seaborn** → Processamento e visualização dos dados.
* **Tkinter + ttkbootstrap** → Interface gráfica.
* **Zipfile, OS, Glob, Shutil** → Manipulação de arquivos.

---

## ✨ Principais Benefícios

* **Eficiência**: elimina processos manuais repetitivos.
* **Padronização**: relatórios organizados e consistentes.
* **Agilidade**: dados resumidos e gráficos em poucos cliques.
* **Escalabilidade**: pode ser adaptado a outros relatórios.

---

## 🚀 Como Usar

### 1. Pré-requisitos

Certifique-se de ter instalado:

* Python **3.9+**
* Google Chrome
* ChromeDriver compatível com sua versão do navegador

Dependências Python:

```bash
pip install selenium pandas matplotlib seaborn ttkbootstrap openpyxl
```

---

### 2. Configuração

No arquivo **`config.py`**:

* Informe o **e-mail** e a **senha** de administrador do Syngoo Talk.
* Defina o caminho da **pasta de downloads** do seu sistema.
* (Opcional) Configure o intervalo de datas (padrão: últimos 3 meses).

---

### 3. Execução

Execute a interface gráfica pelo terminal:

```bash
python controler.py
```

Na interface, escolha a ação desejada:

* **Executar Auto** → Apenas extrai o relatório.
* **Executar Import** → Apenas organiza o arquivo baixado.
* **Executar Relatório** → Apenas processa e analisa os dados.
* **Executar Import + Relatório** → Junta importação e análise.
* **Executar Tudo** → Executa todas as etapas em sequência.

---

### 4. Saída

* Arquivo bruto: `arquivos/notas.xlsx`
* Relatório consolidado: `Resumo_notas/resumo_agentes.xlsx`
* Gráfico exibido em tela: média de notas por atendente.
