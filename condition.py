import pandas as pd

# # Load the dataset
# m = pd.read_excel('C:/Users/ibrah/Desktop/Python/test.xlsx' ,skiprows=range(0,4),header=0)
# # me = m.rename(columns={'PRENOM ET NOM':'Nom', 'adressesmail':'Email',  'mot_passe_provisoire':'PassWord'}, inplace=True)
# # j  = pd.read_json('C:/Users/ibrah/Desktop/Python/test.json')
 
# # print(j.to_excel('test.xlsx'))
# print(m)

dt = pd.read_html('https://fr.wikipedia.org/wiki/France', match='Fonction')

g = dt
print(g)

print('\n================================')
g.rename(columns={0: 'F', 1: 'T'}, inplace=True)
print(g)