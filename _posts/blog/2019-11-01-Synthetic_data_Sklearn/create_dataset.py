
import create_data_functions as cdf
import numpy as np
import pandas as pd
from scipy.io import savemat
from sklearn.datasets import sample_gen_gh as gh
import matplotlib.pyplot as plt



###############################################################################
# Create the dataset
###############################################################################

def make_data(sep_val, nfeat):
    
    X, Y, clust = gh.make_classification(n_samples=1000, 
    									 n_features=nfeat, 
    									 n_informative=10,
    	                				 n_redundant=5, 
    	                				 n_repeated=5, 
    	                				 n_classes=2,
    	                				 n_clusters_per_class=4, 
    	                				 class_sep = sep_val, 
    	                				 shuffle = False)
    
    return X, Y, clust

###############################################################################
# Plot the new communities form kMeans
###############################################################################
    
def plot_3d(X, inds, lab, outPath, write = False, title = '_'):
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    #ax.view_init(elev=25., azim=-21)
    ax.scatter3D(X[:, inds[0]], 
                 X[:, inds[1]], 
                 X[:, inds[2]], 
                 marker='o', 
                 c=lab,
                 s=25, 
                 edgecolor='k')

    plt.title(title)
    plt.show()
    fig.savefig(outPath)

    
    

if __name__ == "__main__":
    
    parDir = 'C:/Users/Gareth/Desktop/'
    nfeat = 25
    inds = np.random.choice(np.arange(nfeat), 3)

    for ii in np.arange(.75, 4.75, 1):

        X, Y, clust = make_data(ii, nfeat)   
        
        plot_3d(X, inds, clust, 
                parDir + 'plot3_' + str(ii) + '.png' , 
                write = True,  
                title = 'Class: 2 Clusters: 4 Sep: ' + str(ii))

ff = np.loadtxt('C:/Users/Gareth/Desktop/samp_arr.txt', delimiter=',')
sns.heatmap(ff) # cmap="YlGnBu", 