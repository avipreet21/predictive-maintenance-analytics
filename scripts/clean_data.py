import pandas as pd

df = pd.read_csv("data/ai4i2020.csv")

df =df.drop(columns=['UDI', 'Product ID'])

df =df.rename(columns={'TWF': 'Tool wear failure', 'HDF': 'Heat dissipation failure', 'PWF': 'Power failure', 'OSF': 'Overstrain failure', 'RNF': 'Random failure'}, inplace=False)


print("Cleaned dataset:")
print(df.head())