
import create_data_functions as cdf
import numpy as np
import pandas as pd
from scipy.io import savemat
from sklearn.datasets import sample_gen_gh as gh
import matplotlib.pyplot as plt



###############################################################################
# Create the dataset
###############################################################################

def make_data(sep_val):
    
    X, Y, clust = gh.make_classification(n_samples=1000, 
    									 n_features=3, 
    									 n_informative=3,
    	                				 n_redundant=0, 
    	                				 n_repeated=0, 
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
    inds = np.array([0, 1, 2])
    
    for ii in np.arange(.75, 4.75, 1):

        X, Y, clust = make_data(ii)   
        
        plot_3d(X, inds, clust, 
                parDir + 'plot3_' + str(ii) + '.png' , 
                write = True,  
                title = 'Class: 2 Clusters: 4 Sep: ' + str(ii))
