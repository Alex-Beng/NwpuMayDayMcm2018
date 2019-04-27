import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


class DataPresentation:
    def __init__(self, scalars):
        self.scalars = scalars
    def LowDim(self, n_dim):
        pca=PCA(n_components=n_dim)
        return pca.fit_transform(self.scalars)

    def VecPic(self):
        pca=PCA(n_components=2)
        scalars = pca.fit_transform(self.scalars)

        former80=scalars[0:79,:]
        latter40=scalars[80:119,:]
        plt.scatter(former80[:,0], former80[:,1], marker='x')
        plt.scatter(latter40[:,0], latter40[:,1], marker='o')
        plt.show()

if __name__ == "__main__":
    pass
