# Automatiser l'analyse exploratoire préliminaire 

import pandas as pd
from ydata_profiling import ProfileReport

# Charger les données
df_data = pd.read_csv("C:/Users/ibrah/Desktop/Python/a.csv", parse_dates=['Date'])

# Générer le rapport
profile = ProfileReport(
    df_data,
    # title="Analyse du marché boursière"
)

# Afficher le rapport dans le notebook
profile.to_notebook_iframe()

# Exporter le rapport au format HTML
profile.to_file('analyse.html')

