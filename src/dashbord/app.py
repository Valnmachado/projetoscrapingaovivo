import streamlit as st
import pandas as pd
import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('../data/quotes.db')

# Carregar os dados da tabela "mercadolivre_itens" em um DataFrame pandas
df = pd.read_sql_query("SELECT * FROM mercadolivre_itens", conn)

# Fechar a conexão com o bonco de dados
conn.close()

# Titulo da aplicação
st.title('Pesquisa de Mercado - Tênis Esportivos no Mercado Livre')

# Melhorar o layout com colunas para KPIs
st.subheader('KPIs principais do sistema')
col1, col2, col3 = st.columns(3)
#st.write(df)

# KPI 1: Número total de itens
total_itens = df.shape[0]
col1.metric(label="Número total de Itens", value=total_itens)

# KPI 2: Número de marcas únicas
unique_brands = df['brand'].nunique()
col2.metric(label="Número de Marcas Únicas", value=unique_brands)

# KPI 3: Preço Médio novo ( em reais )
average_new_price = df['new_price'].mean()
col3.metric(label="Preço Médio Novo (R$)", value=f"{average_new_price:.2f}")


