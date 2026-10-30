
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler


data = pd.read_csv("Mall_Customers.csv")
features = data[["Age", "Annual Income (k$)", "Spending Score (1-100)"]]
scaled = StandardScaler().fit_transform(features)
tree = linkage(scaled, method="ward")
dendrogram(tree)
plt.axhline(y=15, color="red", linestyle="--")
plt.title("Customer Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Distance")
plt.show()

model = AgglomerativeClustering(n_clusters=2, linkage="ward")
data["Cluster"] = model.fit_predict(scaled)
print(data["Cluster"].value_counts())
print(data[["CustomerID", "Age", "Annual Income (k$)", "Spending Score (1-100)", "Cluster"]].head(20))
