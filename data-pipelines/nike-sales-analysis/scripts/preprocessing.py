import pandas as pd
import numpy as np

def preprocess_data(df):

    # 1. suppression des doublons
    df = df.drop_duplicates(subset="Order_ID")
    # 2. conversion des dates
    df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
    # 3. valeurs manquantes
    df['Units_Sold'] = df['Units_Sold'].fillna(df['Units_Sold'].median())
    df['MRP'] = df['MRP'].fillna(df['MRP'].median())
    df['Discount_Applied'] = df['Discount_Applied'].fillna(0)
    df['Revenue'] = df['Revenue'].fillna(0)
    df['Profit'] = df['Profit'].fillna(0)
    df['Region'] = df['Region'].fillna(df['Region'].mode()[0])
    df['Gender_Category'] = df['Gender_Category'].fillna("Unknown")
    # 4. Correction des incohérences
    df.loc[df['Units_Sold'] < 0, 'Units_Sold'] = abs(df['Units_Sold'])
    df.loc[df['Discount_Applied'] > 100, 'Discount_Applied'] = 100
    df.loc[df['MRP'] <= 0, 'MRP'] = df['MRP'].median()
    # 5. Nettoyage des régions
    df['Region'] = df['Region'].str.lower().str.strip()
    df['Region'] = df['Region'].replace({
        'delhii': 'delhi',
        'banglore': 'bangalore'
    })
    # 6. encodage
    df = pd.get_dummies(df, columns=['Sales_Channel', 'Gender_Category'], drop_first=True)
    # 7. normalisation (Min-Max)
    for col in ['Units_Sold', 'MRP', 'Revenue', 'Profit']:
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    # 8. colonne dérivée
    df['Profit_Margin'] = df['Profit'] / (df['Revenue'] + 0.0001)

    return df
