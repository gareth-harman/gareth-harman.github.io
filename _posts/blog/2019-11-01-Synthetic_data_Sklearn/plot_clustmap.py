
import create_data_functions as cdf
import numpy as np
import pandas as pd
from scipy.io import savemat
from sklearn.datasets import sample_gen_gh as gh
import matplotlib.pyplot as plt
import seaborn as sns

if 'X' in locals():
    
    X, Y, clust = gh.make_classification(n_samples=1000, 
    									 n_features=55, 
    									 n_informative=50,
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

#lut = dict(zip(set(clust[inds_0]), sns.color_palette("RdBu_r", len(set(clust[inds_0])))))
#row_colors = pd.DataFrame(clust[inds_0])[0].map(lut)
#
##Create additional row_colors here
#lut2 = dict(zip(set(Y[inds_0]), sns.color_palette("RdBu_r", len(set(Y[inds_0])))))
#row_colors2 = pd.DataFrame(Y[inds_0])[0].map(lut2)
#
#g=sns.clustermap(X[inds_0, 1:10], col_cluster=False, cmap='coolwarm', row_colors=[row_colors, row_colors2])
#plt.show()

lut = dict(zip(set(clust[inds_0]),sns.cubehelix_palette(len(set(clust[inds_0])))))
row_colors = pd.DataFrame(clust[inds_0])[0].map(lut)

g=sns.clustermap(pd.DataFrame(X[inds_0, 1:50]), cmap='coolwarm', row_colors=row_colors) # col_cluster=False, 
plt.show()


lut = dict(zip(set(clust[inds_1]), sns.cubehelix_palette(len(set(clust[inds_1])), start=2, rot=0, dark=0, light=.95, reverse=True)))
row_colors = pd.DataFrame(clust[inds_1])[0].map(lut)

g=sns.clustermap(pd.DataFrame(X[inds_1, 1:50]), cmap='coolwarm', row_colors=row_colors) # col_cluster=False, 
plt.show()

lut = dict(zip(set(clust),sns.cubehelix_palette(len(set(clust)))))
row_colors = pd.DataFrame(clust)[0].map(lut)

g=sns.clustermap(pd.DataFrame(X[:, 1:50]), cmap='mako', row_colors=row_colors) # col_cluster=False, 
plt.show()