import pandas as pd 

df = pd.read_excel('entrada e saida.xlsx')

df.to_csv('dados.csv', index=False)