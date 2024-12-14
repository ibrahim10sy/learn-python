import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
data = {
    "ID": range(1, 21),
    "Age": [25, 32, None, 40, 29, None, 35, 22, None, 28, 26, 31, None, 45, 34, 38, None, 27, 30, None],
    "Genre": [
        "Femme", "Homme", "Femme", "Non-binaire", "Homme", "Femme", 
        "Homme", "Femme", "Non-binaire", "Homme", "Femme", "Homme", 
        "Non-binaire", "Homme", "Femme", "Femme", "Homme", "Homme", "Femme", "Non-binaire"
    ],
    "Préfère_Végétarien": [
        "Oui", None, "Non", "Oui", "Non", None, "Non", "Oui", "Non", None,
        "Oui", "Non", None, "Oui", "Non", None, "Oui", "Oui", None, "Non"
    ],
    "Score_Satisfaction": [
        8, 6, None, 7, 5, 9, 6, 8, None, 7, 8, None, 9, 6, 7, None, 5, 8, 9, None
    ],
}

df_data = pd.read_csv("C:/Users/ibrah/Desktop/Python/a.csv", parse_dates=['Date'])
df_data.drop(['OpenInt'], axis='columns', inplace=True)
# df_data.to_csv("a.csv",index=False)
df_data['ProfitJ'] = df_data['Close']- df_data['Open']
df_data['Annee'] = df_data['Date'].dt.year
df_data['Mois'] = df_data['Date'].dt.month
df_data['Jours'] = df_data['Date'].dt.day
df_data['Benefice'] = df_data['Volume'] * df_data['ProfitJ']
df_data['ProfitA'] = df_data[['Benefice','Annee']].groupby(by='Annee').agg('sum')

print(df_data.head())
# print(df_data['Age'].astype(object))
# print(df_data['Age'].unique())

# print(df_data)
# Suppression de la colonne
# df_data.drop(['Score_Satisfaction'], axis='columns',inplace=True)

# Affichage de la description du dataframe
# print(df_data.describe())

# Affichage de la somme des valeurs nulls
# print(df_data.isnull().sum())

# Visualisation des valeurs nulls
# sb.heatmap(df_data.isnull(), cbar=True, cmap='viridis',)
# plt.show()
# print("\n================================")

#stratégie de gestion

# Supprime les lignes avec des valeurs manquantes
# df_data.dropna(axis=0, inplace=True)
# print(df_data)

# print("================================")
# df_data.dropna(axis=1, inplace=True)  # Supprime les colonnes avec des valeurs manquante
# print(df_data)

# Remplacer les valeurs manquantes
# Remplace age par la moyenne
# print("================================")
# df_data['Age'].fillna(df_data["Age"].mean(), inplace=True)
# df_data["Préfère_Végétarien"].fillna("Inconnu", inplace=True)

# df_data['Score_Satisfaction'].fillna(df_data["Score_Satisfaction"].mean(), inplace=True)
# print(df_data)
# plt.boxplot(df_data['Age'] )
# plt.show()
# print(df_data.isnull().sum())  # Vérifie qu'il n'y a plus de valeurs manquantes
# df_data.to_csv("donnees_nettoyees.csv", index=False)

# calcule de valeur extreme
# q1 = df_data["Age"].quantile(0.25)
# q3 = df_data["Age"].quantile(0.75)
# iqr =q3-q1

# print(iqr)
# print("================================")
# quart1 = q1 - 1.5 * iqr
# quart2 = q3 - 1.5 * iqr

# outlier = ((df_data["Age"] < quart1) | (df_data["Age"] > quart2))
# print(outlier)
#  Imputation avancée
# imputer = KNNImputer(n_neighbors=3)
# df_imputed = imputer.fit_transform(df_data)
# df = pd.DataFrame(df_imputed, columns=df_data.columns)