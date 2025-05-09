import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# ✅ Primeira chamada obrigatória
st.set_page_config(page_title="Análise de Intervalos de Confiança", layout="centered")

# 🎨 Estilo lavanda profunda embutido
st.markdown("""
<style>
    header {visibility: hidden;}
    .viewerBadge_container__1QSob {visibility: hidden;}
    .main .block-container {
        padding-top: 2rem;
        background-color: white;
        border: none;
    }
    body, .main, .block-container {
        background-color: white !important;
        color: #3e3553;
        font-family: 'Segoe UI', sans-serif;
        margin: 0;
    }
    section[data-testid="stSidebar"] {
        background-color: #5e4b8b !important;
        color: white !important;
    }
    section[data-testid="stSidebar"] * {
        color: white !important;
    }
    h1, h2, h3, h4 {
        color: #4a3d6a;
    }
    .stSelectbox > div > div {
        background-color: white !important;
        color: #5e4b8b !important;
    }
    .lavender-box {
        background-color: #ede6fa;
        border-left: 6px solid #b89fe6;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 25px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

st.title("🔍 Intervalos de Confiança por Categoria de Estação")

@st.cache_data
def load_data():
    df = pd.read_excel("dados_metais_com_categoria.xlsx")
    df.columns = df.columns.str.strip().str.title()
    return df

df = load_data()

st.markdown('<div class="lavender-box">', unsafe_allow_html=True)
st.subheader("🧾 Dados Carregados")
st.dataframe(df, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="lavender-box">', unsafe_allow_html=True)
st.subheader("📘 Dicionário das Colunas")
st.markdown("""
- **Estação**: Código da estação de coleta.
- **Categoria**: Incidente (próximo), Medio, Longe.
- **Arsênio Total**, **Ferro Dissolvido**, **Manganês Total**: Concentrações dos metais (μg/L).
""")
st.markdown('</div>', unsafe_allow_html=True)

grupos = {
    "INCIDENTE": ["RD009", "RD075", "RD074", "RD059"],
    "LONGES": ["RD095", "RD085"],
    "MEDIOS": ["RD083", "RD039"]
}

colunas_numericas = df.select_dtypes(include=np.number).columns.tolist()
coluna_selecionada = st.selectbox("Selecione o tipo de metal para análise:", colunas_numericas)

def calcular_ic(dados, alpha=0.05):
    n = len(dados)
    media = np.mean(dados)
    erro_padrao = stats.sem(dados, nan_policy='omit')
    margem_erro = stats.t.ppf(1 - alpha/2, df=n-1) * erro_padrao
    return media, media - margem_erro, media + margem_erro

for grupo_nome, regioes in grupos.items():
    st.subheader(f"📊 Categoria: {grupo_nome}")
    grupo_df = df[df["Estação"].isin(regioes)]
    valores_categoria = grupo_df[coluna_selecionada].dropna()

    if not valores_categoria.empty:
        media_cat, ic_min_cat, ic_max_cat = calcular_ic(valores_categoria)
        st.markdown(f"**Resumo da Categoria `{grupo_nome}`**")
        st.write(f"Média geral: `{media_cat:.2f}`, IC 95%: [`{ic_min_cat:.2f}`, `{ic_max_cat:.2f}`]")

        fig_cat, ax_cat = plt.subplots()
        sns.histplot(valores_categoria, kde=True, ax=ax_cat, color='mediumpurple')
        ax_cat.axvline(ic_min_cat, color='red', linestyle='--', label='IC Min')
        ax_cat.axvline(ic_max_cat, color='red', linestyle='--', label='IC Max')
        ax_cat.axvline(media_cat, color='green', linestyle='-', label='Média')
        ax_cat.set_title(f'Distribuição Geral - {grupo_nome}')
        ax_cat.legend()
        st.pyplot(fig_cat)

    for estacao in regioes:
        estacao_df = grupo_df[grupo_df["Estação"] == estacao]
        valores = estacao_df[coluna_selecionada].dropna()

        if valores.empty:
            continue

        media, ic_min, ic_max = calcular_ic(valores)
        st.markdown(f"**Estação `{estacao}`**")
        st.write(f"Média: `{media:.2f}`, IC 95%: [`{ic_min:.2f}`, `{ic_max:.2f}`]")

        fig, ax = plt.subplots()
        sns.histplot(valores, kde=True, ax=ax, color='skyblue')
        ax.axvline(ic_min, color='red', linestyle='--', label='IC Min')
        ax.axvline(ic_max, color='red', linestyle='--', label='IC Max')
        ax.axvline(media, color='green', linestyle='-', label='Média')
        ax.set_title(f'Distribuição - {estacao}')
        ax.legend()
        st.pyplot(fig)

# --- Comparação geral entre categorias ---
st.markdown('<div class="lavender-box">', unsafe_allow_html=True)
st.subheader("📊 Comparação entre Categorias")

df_filtrado = df[df['Categoria'].isin(['Incidente', 'Medio', 'Longe'])][['Categoria', 'Arsênio Total']].dropna()

def plot_boxplot_violin(df_filtrado):
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    sns.boxplot(data=df_filtrado, x='Categoria', y='Arsênio Total', palette='Pastel1', ax=axs[0])
    axs[0].set_title('Boxplot - Arsênio Total por Categoria')
    axs[0].set_ylabel('ARSÊNIO TOTAL')
    axs[0].set_xlabel('Categoria')

    sns.violinplot(data=df_filtrado, x='Categoria', y='Arsênio Total', palette='Pastel2', ax=axs[1])
    axs[1].set_title('Violin Plot - Arsênio Total por Categoria')
    axs[1].set_ylabel('ARSÊNIO TOTAL')
    axs[1].set_xlabel('Categoria')

    plt.tight_layout()
    return fig

fig_comparativo = plot_boxplot_violin(df_filtrado)
st.pyplot(fig_comparativo)
st.markdown('</div>', unsafe_allow_html=True)
