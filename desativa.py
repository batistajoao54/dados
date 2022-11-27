import pandas as pd


def desativa():
    df = pd.read_csv('dados.csv')
    df_desativado = df[df['STATUS'] == "DESATIVAR"].copy()
    lista_os = list(df_desativado['OS'].unique())
    #print(lista_os)
    #Tirando as OS desativada do nosso arquivo
    for i in lista_os:
        df = df[df['OS'] != i]
        df = df   
    #print(df)
    return df


def os_de():
    df = pd.read_csv('dados.csv')
    df_desativado = df[df['STATUS'] == "DESATIVAR"].copy()
    lista_os = list(df_desativado['OS'].unique())
    return lista_os


def desativa_os():
    df = pd.read_csv('dados_os.csv')
    lista_os = os_de()
    #print(lista_os)
    
    for i in lista_os:
        df = df[df["OS"] != i]
        df = df
    #print("NI", df)
    return df
    
 



if "__main__" == __name__:
    desativa()
    desativa_os()
    os_de()