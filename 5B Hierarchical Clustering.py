import scipy.cluster.hierarchy as shc
import matplotlib.pyplot as plt

# Perform hierarchical clustering
dendrogram = shc.dendrogram(shc.linkage(X, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Sample index')
plt.ylabel('Distance')
plt.show()

# Cut the dendrogram to determine the number of clusters
num_clusters = 3
labels = shc.fcluster(shc.linkage(X, method='ward'), num_clusters, criterion='maxclust')

# Visualize the clusters
plt.scatter(X[labels == 1, 0], X[labels == 1, 1], s=100, c='red', label='Cluster 1')
plt.scatter(X[labels == 2, 0], X[labels == 2, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(X[labels == 3, 0], X[labels == 3, 1], s=100, c='green', label='Cluster 3')
plt.title('Hierarchical Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()
