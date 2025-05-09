import streamlit as st
import pandas as pd

# --- Configuração da página ---
st.set_page_config(page_title="Dashboard: Qualidade da Água", layout="wide")

# --- Estilo embutido: header oculto e fundo uniforme ---
st.markdown("""
<style>
    header {visibility: hidden;}
    .viewerBadge_container__1QSob {visibility: hidden;}

    .main .block-container {
        padding-top: 2rem;
    }

    body, .main, .block-container {
        background-color: #f9f7fc !important;
        color: #3e3553;
        font-family: 'Segoe UI', sans-serif;
    }

    section[data-testid="stSidebar"] {
        background-color: #5e4b8b !important;
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

    .banner {
        background-color: #5e4b8b;
        color: white;
        padding: 1.5rem;
        text-align: center;
        font-size: 1.5rem;
        font-weight: 600;
        border-radius: 10px;
        margin-bottom: 40px;
        letter-spacing: 0.5px;
    }

    .footer {
        font-size: 0.9rem;
        color: #777;
        text-align: center;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)

# --- Banner de destaque ---
st.markdown('<div class="banner">💧 Monitoramento de Qualidade da Água - Análise Estatística</div>', unsafe_allow_html=True)

# --- Título da Página ---
st.title("📌 Introdução e Preparação")

# --- Seção: Sobre o desastre de Mariana ---
st.markdown('<div class="lavender-box">', unsafe_allow_html=True)
st.subheader("📍 O Desastre de Mariana")

st.markdown("""
Em **5 de novembro de 2015**, ocorreu um dos maiores desastres socioambientais da história do Brasil: o **rompimento da barragem de Fundão**, em **Mariana (MG)**. A barragem, de responsabilidade da empresa **Samarco**, uma joint venture da **Vale** e da **BHP Billiton**, armazenava rejeitos da mineração de ferro.
""")

# Exibe imagem do diretório local (crie uma pasta 'images' e coloque a imagem lá)
col1, col2 = st.columns(2)

with col1:
    st.image("images/mariana_desastre.jpg", caption="Desastre de Mariana", width=300)

with col2:
    st.image("images/rio_doce_afetado.jpg", caption="Contaminação do Rio Doce", width=300)

st.markdown("""
Com o colapso da estrutura, aproximadamente **40 milhões de metros cúbicos** de lama tóxica foram liberados, destruindo o distrito de **Bento Rodrigues**, atingindo comunidades vizinhas e causando **19 mortes**. A onda de rejeitos percorreu mais de **600 km ao longo do Rio Doce**, afetando ecossistemas, o abastecimento de água e meios de subsistência de milhares de pessoas em Minas Gerais e no Espírito Santo.

O material liberado continha **altas concentrações de metais pesados**, como **arsênio, manganês e ferro**, o que gerou impactos ambientais de longo prazo, ainda estudados e monitorados até os dias de hoje. Esse evento serviu como alerta para a fragilidade dos sistemas de contenção da indústria mineradora no Brasil e a urgência de políticas de prevenção e fiscalização mais eficazes.
""")
st.markdown('</div>', unsafe_allow_html=True)

# --- Seção 1: Contexto do Problema ---
st.markdown('<div class="lavender-box">', unsafe_allow_html=True)
st.subheader("🔍 1. Contexto do Problema")
st.markdown("""
A análise da qualidade da água é crucial para garantir a segurança da população e a preservação ambiental.  
Neste projeto, analisamos amostras coletadas em diferentes estações próximas a um **evento de contaminação**. Essas estações foram classificadas como:

- **Incidente**: diretamente afetadas pelo incidente de contaminação;
- **Médios**: localizações próximas ao incidente, com risco potencial de contaminação;
- **Longes**: regiões mais distantes, atuando como controle para a análise comparativa.

Nosso objetivo é aplicar métodos estatísticos (como **intervalos de confiança**) para entender se a diferença na concentração de metais entre esses grupos é estatisticamente significativa.
""")
st.markdown('</div>', unsafe_allow_html=True)

# --- Seção 2: Dataset e Variáveis ---
st.markdown('<div class="lavender-box">', unsafe_allow_html=True)
st.subheader("📊 2. Sobre o Dataset")
st.markdown("""
O dataset utilizado, chamado **`dados_metais_com_categoria.xlsx`**, contém informações sobre concentrações de metais em diferentes estações de coleta de água.

**Principais variáveis:**
""")

data_dict = {
    "Coluna": ["Estação", "Categoria", "Data", "Arsênio total", "Ferro dissolvido", "Manganês total"],
    "Descrição": [
        "Código da estação de coleta de água",
        "Classificação: Incidente, Médio, Longe",
        "Data da amostragem da água",
        "Concentração total de Arsênio (μg/L)",
        "Concentração de Ferro dissolvido (μg/L)",
        "Concentração total de Manganês (μg/L)"
    ]
}
df_dicionario = pd.DataFrame(data_dict)
st.table(df_dicionario)
st.markdown('</div>', unsafe_allow_html=True)

# --- Seção 3: Hipóteses e Perguntas ---
st.markdown('<div class="lavender-box">', unsafe_allow_html=True)
st.subheader("💡 3. Hipóteses e Perguntas Investigativas")
st.markdown("""
Durante a investigação, serão testadas as seguintes hipóteses e levantadas perguntas chave:

- As estações **"Incidente"** apresentam **níveis significativamente mais altos** de metais?
- Estações **"Longe"** têm níveis dentro dos limites aceitáveis?
- O comportamento das concentrações **se mantém constante ao longo do tempo**?
- Existe alguma **diferença estatística significativa** nos grupos identificados?

Essas perguntas serão respondidas por meio da **análise estatística e visualizações**, ao longo do dashboard.
""")
st.markdown('</div>', unsafe_allow_html=True)

# --- Rodapé ---
st.markdown("---")
st.markdown('<div class="footer">🎓 Projeto acadêmico - FIAP | Uso interno e institucional</div>', unsafe_allow_html=True)
