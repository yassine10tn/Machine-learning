import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\Yassine\\Desktop\\projet python cafe sales\\data\\raw\\dirty_cafe_sales.csv", sep=";")

# Remplacer 'ERROR' et 'UNKNOWN' par NaN
df.replace(["ERROR", "UNKNOWN", ""], np.nan, inplace=True)

# Conversion numérique
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors="coerce")
df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors="coerce")

# Imputation
df["Payment Method"].fillna("Unknown", inplace=True)
df["Location"].fillna("Unknown", inplace=True)

df["Quantity"].fillna(df["Quantity"].median(), inplace=True)
df["Price Per Unit"].fillna(df["Price Per Unit"].median(), inplace=True)

# Recalcul du total si manquant
df["Total Spent"] = df["Quantity"] * df["Price Per Unit"]

# Dates
df["Transaction Date"] = pd.to_datetime(
    df["Transaction Date"],
    errors="coerce",
    dayfirst=True
)

print("Nettoyage terminé")
