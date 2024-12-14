import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import plotly.express as ep


df_data = pd.read_csv("C:/Users/ibrah/Desktop/Python/a.csv", parse_dates=['Date'])
df_data.drop(['OpenInt'], axis='columns', inplace=True)

volume = df_data['Volume']

moyenne = np.mean(volume)
mediane = np.median(volume)
mode  = stats.mode(volume)[1]

print(moyenne, mediane,mode)

ep.histogram(volume,x='Volume')
ep.show()