import pandas as pd

df = pd.read_csv("data/ai4i2020.csv")
#Explore the data

print("First 5 rows of the dataset:")

print(df.head())

print("\nSummary statistics:")
print(df.describe())

print("\nColumn names:")
print(df.columns)

print("\n Number of missing values in each column:")
print(df.isnull().sum())

print("\nDataset information:")
print(df.info())

print("\n How many time machine fails?")
print(df['Machine failure'].value_counts())

print("\n failure because of tool wear?")
print(df['TWF'].value_counts())

print("\n failure because of heat dissipation failure?")
print(df['HDF'].value_counts())

print("\n failure because of power failure?")
print(df['PWF'].value_counts())

print("\n failure because of overstrain failure?")
print(df['OSF'].value_counts())

print("\n failure because of random failure?")
print(df['RNF'].value_counts())

