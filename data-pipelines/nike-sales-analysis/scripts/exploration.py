import matplotlib.pyplot as plt
import seaborn as sns

def explore_data(df):
    print("informations générales sur le dataset")
    print(df.info())

    print("\n statistiques descriptives")
    print(df.describe(include='all'))

    print("\n valeurs manquantes par colonne")
    print(df.isnull().sum())

    # distribution des unités vendues
    plt.figure(figsize=(6,4))
    sns.histplot(df['Units_Sold'], kde=True)
    plt.title("distribution of Units Sold")
    plt.show()
