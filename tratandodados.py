import pandas as pd

def enviados(marca='OS001108/03VMp'):
    df = pd.read_csv('dados.csv')
    df_enviados = df[df["STATUS"] == 'ENVIADO'].copy()
    df_enviados['COLADOR'] = 'IDEZ'
    df_enviados2 = df_enviados.groupby(["COLADOR","MARCA","OS","STATUS"]).sum().reset_index()
    df_recebidos = df[df["STATUS"] == 'RECEBIDO'].copy()
    df_recebidos['COLADOR'] = 'IDEZ'
    df_recebidos2 = df_recebidos.groupby(["COLADOR","MARCA","OS","STATUS"]).sum().reset_index()
    df_final = pd.concat([df_enviados2, df_recebidos2])
    df_marca = df_final[df_final['OS'] == marca].copy()
    #print(df_marca.head())
    return df_marca
    
    

if "__main__" == __name__:
    enviados()