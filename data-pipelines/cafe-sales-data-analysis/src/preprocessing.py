import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("C:\\Users\\Yassine\\Desktop\\projet python cafe sales\\data\\raw\\dirty_cafe_sales.csv", sep=";")

# Nettoyage minimal
df.replace(["ERROR", "UNKNOWN", ""], pd.NA, inplace=True)
df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors="coerce")

# Extraction temporelle
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], errors="coerce")
df["Month"] = df["Transaction Date"].dt.month
df["DayOfWeek"] = df["Transaction Date"].dt.dayofweek

# Encodage One-Hot
df_encoded = pd.get_dummies(
    df,
    columns=["Payment Method", "Location"],
    prefix=["pay", "loc"],
    dtype=int
)

# Normalisation
scaler = StandardScaler()
df_encoded["Total_Spent_Std"] = scaler.fit_transform(
    df_encoded[["Total Spent"]]
)

print("Pré-traitement terminé")
