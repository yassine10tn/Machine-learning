import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

# =============================================================
# 1. LOADING & PREPARING DATA
# =============================================================

df = pd.read_csv('data/Mall_Customers.csv')
df.rename(columns={
    'Annual Income (k$)': 'Annual_Income',
    'Spending Score (1-100)': 'Spending_Score'
}, inplace=True)

print(df.head(5))

# =============================================================
# 2. EXPLORATORY DATA ANALYSIS (EDA)
# =============================================================

# Pairplot: shows relationships between all 3 features
sns.pairplot(df[['Age', 'Annual_Income', 'Spending_Score']])
plt.show()
plt.close()

# Scatter plot: Annual Income vs Spending Score
plt.figure(figsize=(10, 6))
plt.scatter(df['Annual_Income'], df['Spending_Score'], s=50)
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.title('Annual Income vs Spending Score')
plt.show()
plt.close()
"""
# =============================================================
# 3. K-MEANS WITH 2 FEATURES (Annual Income & Spending Score)
# =============================================================

X = df[['Annual_Income', 'Spending_Score']]

# -- Elbow Method to find optimal number of clusters --
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method — Optimal Number of Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()
plt.close()

# -- Applying K-Means with 5 clusters (chosen from elbow method) --
kmeans = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10, random_state=0)
y_kmeans = kmeans.fit_predict(X)
df['Cluster'] = y_kmeans

# -- Visualizing clusters --
plt.figure(figsize=(10, 6))
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.title('Customer Segmentation — 2 Features (Annual Income & Spending Score)')
plt.show()
plt.close()
"""

# =============================================================
# 4. K-MEANS WITH 3 FEATURES (Age, Annual Income & Spending Score)
# =============================================================

X = df[['Age', 'Annual_Income', 'Spending_Score']]

# -- Elbow Method to find optimal number of clusters --
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method — Optimal Number of Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()
plt.close()

# -- Applying K-Means with 6 clusters (chosen from elbow method) --
kmeans = KMeans(n_clusters=6, init='k-means++', max_iter=300, n_init=10, random_state=0)
y_kmeans = kmeans.fit_predict(X)
df['Cluster'] = y_kmeans

# -- Visualizing clusters in 3D --
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X.iloc[:, 0], X.iloc[:, 1], X.iloc[:, 2], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
ax.scatter(centers[:, 0], centers[:, 1], centers[:, 2], c='red', s=200, alpha=0.75, marker='X')
ax.set_xlabel('Age')
ax.set_ylabel('Annual Income')
ax.set_zlabel('Spending Score')
ax.set_title('Customer Segmentation — 3 Features (Age, Annual Income & Spending Score)')
plt.show()