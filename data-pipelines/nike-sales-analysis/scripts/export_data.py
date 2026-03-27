def export_clean_data(df, path):
    df.to_csv(path, index=False)
    print(f"données nettoyées exportées vers : {path}")
