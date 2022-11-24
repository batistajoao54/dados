import streamlit as st
import pandas as pd
import plotly.express as px

df_dados = pd.read_csv('dados.csv')
df_dados['MES'] = pd.to_numeric(df_dados['MES'])
df_dados2 = df_dados.sort_values(by=['MES'], ascending=False)
lista_mes = list(df_dados2['MES'].unique()) #mes de acordo com o enviorecebido de sacolas

df_os = pd.read_csv('dados_os.csv')
df_os['MES'] = pd.to_numeric(df_os['MES'])
df_os2 = df_os.sort_values(by=['MES'], ascending=False)
lista_mes2 = list(df_os2['MES'].unique()) #mes de acordo com as datas das os




st.set_page_config(layout= 'wide')

st.markdown("#### PEQUENOS DADOS 'SACOLAS'")

col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    opcao = st.selectbox("MÊS",lista_mes2)

df_marca = df_os[df_os['MES'] == opcao].copy()
df_marca['text'] = df_marca['MARCA'] + " " + df_marca['TAMANHO'] + " " + df_marca['COR']
df_marca2 = df_marca[['COLADOR','MES','DIA','ANO','OS','MARCA','TAMANHO','COR','QUANTIDADE','STATUS','PAGO','text']]
lista_os = list(df_marca2['OS'].unique())

for i in lista_os:
    
    df_junto = df_dados.groupby(['COLADOR','OS','MARCA','TAMANHO','COR','STATUS','PAGO']).sum().reset_index()
    df_junto['text'] = ''
    dados_comp = df_marca2[df_marca2['OS'] == i]
    dados = df_junto[df_junto["OS"] == i]
    
    df = pd.concat([dados_comp, dados])
    
    
    fig = px.bar(df, x="COLADOR", y="QUANTIDADE", color='STATUS',
                barmode='group', height=400, width=700,
                text_auto=True, title=f'SACOLAS {df.iloc[0,11]}')
    
    st.plotly_chart(fig, use_container_width=True)
    
    
    #st.write(df)
    #st.write(f'sacolas {df.iloc[0,11]}')

#st.write(df_marca2)
#st.write(lista_os)



