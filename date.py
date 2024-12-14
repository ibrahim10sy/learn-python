import pandas as pd
import matplotlib.pyplot as plt


df_data = pd.read_csv("C:/Users/ibrah/Desktop/Python/a.csv", parse_dates=['Date'])
df_data.drop(['OpenInt'], axis='columns', inplace=True)
# df_data.to_csv("a.csv",index=False)
df_data['ProfitJ'] = df_data['Close']- df_data['Open']
df_data['Annee'] = df_data['Date'].dt.year
df_data['Mois'] = df_data['Date'].dt.month
df_data['Jours'] = df_data['Date'].dt.day
df_data['Benefice'] = df_data['Volume'] * df_data['ProfitJ']
df_data['ProfitA'] = df_data[['Benefice','Annee']].groupby(by='Annee').agg('sum')
