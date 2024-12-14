# Produire et manupiler des agregations avec pandas

import pandas as pd
import matplotlib.pyplot as plt


df_data = pd.read_csv("C:/Users/ibrah/Desktop/Python/a.csv", parse_dates=['Date'])
df_data.drop(['OpenInt'], axis='columns', inplace=True)
# print(df_data.head())

print("=========== Calcul de la moyenne high et low ==========")
# df_data['high_mean'] = df_data[['High', 'Low']].mean()
mean_high_low = df_data[['High', 'Low']].mean()
# print(mean_high_low)
# print(df_data.head())

print("=========== Calcul de la moyenne des volumes ==========")
volume_mean = df_data['Volume'].mean()
# print(volume_mean)
# Somme total des volumes 
total_volume = df_data['Volume'].sum()

# print(f"Total Volume: {total_volume}")
print("=========== Calcul de la somme des profits ==========")
df_data['Profit'] = df_data['Close'] - df_data['Open']
# Profil total 
total_profit = df_data['Profit'].sum()
# print(total_profit)

print("=========== Calcul de la benefice total ==========")
df_data['Benefice'] = df_data['Profit']  * df_data['Volume']
# print(df_data.head())

print("=========== regroupement par mois ==========")
df_data['Month'] = df_data['Date'].dt.month
# print(df_data.head())

# Ajout d'une colonne pour le mois
df_data['Months'] = df_data['Date'].dt.to_period('M')

# Groupement par mois et calcul de la moyenne
monthly_mean = df_data.groupby('Months').mean()
# print(monthly_mean)

print("===========groupement par mois le volume==========")

df_data['Volume_Months'] = df_data.groupby('Month') ['Volume'].sum()
df_data['Benefice_month'] = df_data.groupby('Month') ['Benefice'].sum()
# print(df_data[['Month', 'Benefice']])
# print(df_data.head())

print("======== Variation journalière ==========")
df_data['Daily Change (%)'] = ((df_data['Close'] - df_data['Open']) / df_data['Open']) * 100
# print(df_data[['Date', 'Daily Change (%)']])

print("=========Moyenne mobile sur 3 jours pour Close ========")

df_data['3-Day Moving Avg'] = df_data['Close'].rolling(window=3).mean()
# print(df_data[['Date', 'Close', '3-Day Moving Avg']])

print("======= totaux hebdomadaires=========")

df_data['Weekly Total'] = df_data.groupby(df_data['Date'].dt.isocalendar().week)['Close'].sum()
# print(df_data['Weekly Total'])

print("========= Utilisation de plusieurs fonctions d'agrégation =========")
aggregated = df_data.agg({
    'Open': ['mean', 'min', 'max'],
    'Close': ['mean', 'std'],
    'Volume': ['sum']
})
# print(aggregated)

print("======== Visualisation des agrégations ==========")
plt.plot(df_data['Date'], df_data['Close'], label='Close Price')
plt.plot(df_data['Date'], df_data['3-Day Moving Avg'], label='3-Day Moving Avg', linestyle='--')
plt.legend()
plt.show()