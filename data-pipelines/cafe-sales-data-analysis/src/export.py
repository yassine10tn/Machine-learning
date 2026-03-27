import pandas as pd

df = pd.read_csv("C:\\Users\\Yassine\\Desktop\\projet python cafe sales\\data\\raw\\dirty_cafe_sales.csv", sep=";")

df.replace(["ERROR", "UNKNOWN", ""], pd.NA, inplace=True)
df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors="coerce")

df.to_csv(
    "data/processed/coffee_sales_cleaned.csv",
    index=False
)

print("Export CSV effectué")
