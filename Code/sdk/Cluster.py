import pickle
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

class Cluster:
    def __init__(self, scalars):
        self.scalars = scalars 
    def Cluster(self):
        kmeans_cluster = KMeans(n_clusters=2)
        kmeans_cluster.fit(self.scalars)
        self.labels = kmeans_cluster.labels_
    def ToPics(self):
        pca = PCA(n_components=2)
        two_dim_scalars = pca.fit_transform(self.scalars)
        for i in range(len(two_dim_scalars)):
            if i <=79:
                if self.labels[i] == 0:
                    plt.scatter(two_dim_scalars[i][0], two_dim_scalars[i][1], marker='x', c='yellow')
                else:
                    plt.scatter(two_dim_scalars[i][0], two_dim_scalars[i][1], marker='x', c='red')
            else:
                if self.labels[i] == 0:
                    plt.scatter(two_dim_scalars[i][0], two_dim_scalars[i][1], marker='o', c='yellow')
                else:
                    plt.scatter(two_dim_scalars[i][0], two_dim_scalars[i][1], marker='o', c='red')
        plt.show() 
if __name__ == "__main__":
    pass
