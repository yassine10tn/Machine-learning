def validate_data(df):
    print("vérification après traitement\n")

    print("valeurs manquantes restantes :")
    print(df.isnull().sum())

    print("\ntypes de données :")
    print(df.dtypes)

    # verifier les valeurs négative uniquement dans les colonnes num
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    print("\nvaleurs négatives dans les colonnes numériques ?")
    print((df[numeric_cols] < 0).sum())
