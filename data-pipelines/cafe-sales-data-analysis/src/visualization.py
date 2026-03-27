import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\Yassine\\Desktop\\projet python cafe sales\\data\\raw\\dirty_cafe_sales.csv", sep=";")
df.replace(["ERROR", "UNKNOWN", ""], pd.NA, inplace=True)
df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors="coerce")

# Agrégation
sales_by_item = df.groupby("Item")["Total Spent"].sum()

# Barplot
sales_by_item.plot(kind="bar")
plt.title("Total des ventes par produit")
plt.ylabel("Total Spent")
plt.tight_layout()
plt.savefig("outputs/figures/sales_by_item.png")
plt.show()

# Histogramme
df["Total Spent"].hist(bins=10)
plt.title("Distribution des dépenses")
plt.xlabel("Total Spent")
plt.savefig("outputs/figures/total_spent_distribution.png")
plt.show()
