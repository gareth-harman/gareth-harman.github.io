
import create_data_functions as cdf
import numpy as np
import pandas as pd
from scipy.io import savemat
from sklearn.datasets import sample_gen_gh as gh
import matplotlib.pyplot as plt
import seaborn as sns

n_imp = 25

X, Y, clust = gh.make_classification(n_samples=1000, 
									 n_features=n_imp+5, 
									 n_informative=n_imp,
	                				 n_redundant=5, 
	                				 n_repeated=0, 
	                				 n_classes=2,
	                				 n_clusters_per_class=4, 
	                				 class_sep = 2.5, 
	                				 shuffle = False)

inds_0 = np.where(Y == 0)[0]
inds_1 = np.where(Y == 1)[0]

clust_0 = clust[inds_0]
clust_1 = clust[inds_1]


#lut = dict(zip(set(clust[inds_0]),sns.cubehelix_palette(len(set(clust[inds_0])))))
#row_colors = pd.DataFrame(clust[inds_0])[0].map(lut)
#
#g=sns.clustermap(pd.DataFrame(X[inds_0, 1:50]), cmap='coolwarm', row_colors=row_colors) # col_cluster=False, 
#plt.show()


#lut = dict(zip(set(clust[inds_1]), sns.cubehelix_palette(len(set(clust[inds_1])), start=2, rot=0, dark=0, light=.95, reverse=True)))
#row_colors = pd.DataFrame(clust[inds_1])[0].map(lut)
#
#g=sns.clustermap(pd.DataFrame(X[inds_1, 1:50]), cmap='coolwarm', row_colors=row_colors) # col_cluster=False, 
#plt.show()

lut = dict(zip(set(clust),sns.color_palette("RdYlBu", len(set(clust)))))
row_colors = pd.DataFrame(clust)[0].map(lut)

g=sns.clustermap(pd.DataFrame(X[:, 1:n_imp]), col_cluster=True, cmap='RdBu', row_colors=row_colors) # 
plt.title('HIerarchical Clustering')
plt.show()


from sklearn.decomposition import PCA

pca = PCA(2)  # project from 64 to 2 dimensions
projected = pca.fit_transform(X)

    
#fig = plt.figure()
#ax = fig.gca(projection='3d')
##ax.view_init(elev=25., azim=-21)
#ax.scatter3D(projected[:, 0],
#             projected[:, 1], 
#             projected[:, 2],
#             marker='o', 
#             c=clust,
#             s=25, 
#             edgecolor='k')
#
#plt.title('PCA Plot')
#plt.show()
#fig.savefig(outPath)
plt.figure()
plt.scatter(projected[:, 0], projected[:, 1],
            c=clust, edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('Spectral', len(set(clust))))
plt.xlabel('component 1')
plt.ylabel('component 2')
plt.colorbar();
plt.title('PCA')

#plt.scatter(projected[:, 0], projected[:, 1],
#            c=digits.target, edgecolor='none', alpha=0.5,
#            cmap=plt.cm.get_cmap('spectral', 10))
#plt.xlabel('component 1')
#plt.ylabel('component 2')
#plt.colorbar();

from sklearn.manifold import TSNE

X_embedded = TSNE(n_components=2).fit_transform(X)

plt.figure()
plt.scatter(X_embedded[:, 0], X_embedded[:, 1],
            c=clust, edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('Spectral', len(set(clust))))
plt.xlabel('component 1')
plt.ylabel('component 2')
plt.colorbar();
plt.title('TSNE')
