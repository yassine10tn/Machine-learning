import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_data(df):
    """
    Fonction pour visualiser les données essentielles du dataset Nike
    Affiche :
    - Heatmap des corrélations entre colonnes numériques
    - Histogramme de Revenue
    - Barplot du Revenue par Product_Line
    """


    numeric_df = df.select_dtypes(include=['int64', 'float64'])
    #  heatmap des corrélations
    # ----------------------------
    corr = numeric_df.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(" matrice de corrélation des colonnes numériques")
    plt.show()

    #histogramme Revenue

    plt.figure(figsize=(8, 5))
    sns.histplot(df['Revenue'], bins=30, kde=True, color='blue')
    plt.title("distribution de Revenue")
    plt.show()

    # barplot Revenue par product line
    plt.figure(figsize=(8, 5))
    sns.barplot(x='Product_Line', y='Revenue', data=df, estimator=sum, ci=None, palette='viridis')
    plt.title("Revenue total par Product_Line")
    plt.ylabel("Revenue")
    plt.xlabel("Product line")
    plt.xticks(rotation=45)
    plt.show()

    print("visualisation terminée !")
