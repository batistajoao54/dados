import streamlit as st
import pandas as pd
import plotly.express as px
import tratandodados
import desativa

df_dados = desativa.desativa()
df_dados['MES'] = pd.to_numeric(df_dados['MES'])
df_dados2 = df_dados.sort_values(by=['MES'], ascending=False)
lista_mes = list(df_dados2['MES'].unique()) #mes de acordo com o enviorecebido de sacolas

#df_os = pd.read_csv('dados_os.csv')
df_os = desativa.desativa_os()
df_os['MES'] = pd.to_numeric(df_os['MES'])
df_os2 = df_os.sort_values(by=['MES'], ascending=False)
lista_mes2 = list(df_os2['MES'].unique()) #mes de acordo com as datas das os
lista_marca = list(df_dados2["MARCA"].unique()) #selecionando as marcas



st.set_page_config(layout= 'wide')

st.markdown("#### PEQUENOS DADOS 'SACOLAS'")

col1,col2,col3,col4,col5 = st.columns([2,7,0.1,0.1,0.1])

with col1:
    opcao = st.selectbox("MARCA",lista_marca)

df_marca = df_os[df_os['MARCA'] == opcao].copy()
df_marca['text'] = df_marca['MARCA'] + " " + df_marca['TAMANHO'] + " " + df_marca['COR'] + " || " + df_marca['OS']
df_marca2 = df_marca[['COLADOR','MES','DIA','ANO','OS','MARCA','TAMANHO','COR','QUANTIDADE','STATUS','PAGO','text']]
#lista_os = desativa.os_de()
lista_os = list(df_marca2['OS'].unique())

with col2:
    opcao2 = st.multiselect('ADICIONE AS OS',lista_os,lista_os[-1])


for i in opcao2:
    
    df_junto = df_dados.groupby(['COLADOR','OS','MARCA','TAMANHO','COR','STATUS','PAGO']).sum().reset_index()
    df_junto['text'] = ''
    dados_comp = df_marca2[df_marca2['OS'] == i]
    dados = df_junto[df_junto["OS"] == i]
    
    df = pd.concat([dados_comp, dados])
    df_fora = tratandodados.enviados(i)
    df_certo = pd.concat([df, df_fora])
    
    fig = px.bar(df_certo, x="COLADOR", y="QUANTIDADE", color='STATUS',
                barmode='group', height=400, width=700,
                text_auto=True, title=f'SACOLAS {df.iloc[0,11]}')
    
    st.plotly_chart(fig, use_container_width=True)
    
    
    #st.write(df)
    #st.write(f'sacolas {df.iloc[0,11]}')

st.write("ÚLTIMA ATUALIZAÇÃO: 25-11-2022")
#st.write(lista_os)



