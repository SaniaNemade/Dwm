#Agglomerative
#heirarchial clustering
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt

num_data_points = int(input("Enter the no. of data points: "))
data_points = [list(map(float, input(f"Enter the coordinates for data point {i+1} (x y): ").split())) for i in range(num_data_points)]
X = np.array(data_points)
Z = linkage(X, 'complete')
merging_steps = []
data_points = X.tolist()

for i in range(len(Z)):
    threshold = Z[i, 2]
    clusters = fcluster(Z, threshold, criterion='distance')
    step = []
    for cluster_id in np.unique(clusters):
        data_point_indices = np.where(clusters == cluster_id)[0]
        data_point_cluster = [data_points[i] for i in data_point_indices]
        step.append(data_point_cluster)
    merging_steps.append((threshold, step))

for i, (threshold, step) in enumerate(merging_steps):
    print(f"Step {i+1}:")
    for j, merged_clusters in enumerate(step):
        if len(merged_clusters) > 1:
            print(f"Merging {merged_clusters} at threshold {threshold:.2f}")
    print()

# Plot dendrogram
dendrogram(Z, labels=[str(point) for point in X])
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Data point')
plt.ylabel('Distance')
plt.show()
