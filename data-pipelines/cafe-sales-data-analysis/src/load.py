import pandas as pd

# Lecture des données
df = pd.read_csv("data/raw/dirty_cafe_sales.csv", sep=";")


# Exploration initiale
print("Aperçu des données :")
print(df.head())

print("\nInformations générales :")
print(df.info())

print("\nDimensions :", df.shape)

print("\nTypes de données :")
print(df.dtypes)

# Statistiques descriptives
print("\nStatistiques descriptives :")
print(df.describe(include='all'))
