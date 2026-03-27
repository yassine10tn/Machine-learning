import pandas as pd

df = pd.read_csv("data/processed/coffee_sales_cleaned.csv")

print("Valeurs manquantes par colonne :")
print(df.isna().sum())

print("\nDoublons :", df.duplicated().sum())

print("\nTypes de données :")
print(df.dtypes)

print("\nStatistiques finales :")
print(df.describe())
