#!/usr/bin/python3


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics as met
import sklearn.datasets as dt
import seaborn as sns
import copy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
import numpy as np


################################################################
# Function to create the datasets
################################################################

def create_set(sep, nfeat, nfeat_i, nfeat_r, n=2500, nclust=4):
    
    # Create dataset 
    X, Y = dt.make_classification(n_samples=n,
                                    n_clusters_per_class=nclust,
                                    class_sep=sep,
                                    n_features=nfeat, 
                                    n_redundant=nfeat_r, 
                                    n_informative=nfeat_i)
    
    return(X, Y)


################################################################
# Function to get communities using kmeans
################################################################

def kmeans_comm_get(X, Y):

    # Store kmeans labels for each group
    kmeans_lab = {'k_labs': [],
                  'group_inds': [],
                  'group_id': []}

    tot_lab = np.zeros(len(Y))

    for ii in np.unique(Y):

            # Get indices of current group
            inds = np.where(Y == ii)[0]

            # Split dataset for these indices
            X_curr = X[inds, :]

            # Run kmeans to get clusters
            kmeans = KMeans(n_clusters=4, 
                            random_state=0)

            # Fit the kmeans to our data
            kfit = kmeans.fit(X_curr) 

            # Add it to the overall
            kmeans_lab['k_labs'].append(kfit.labels_)
            kmeans_lab['group_inds'].append(inds)
            kmeans_lab['group_id'].append(ii)

            # Get labels for overall
            tot_lab[inds] = kfit.labels_ + (10 * ii)

    return(kmeans_lab, tot_lab)


################################################################
# Function to permute classes
################################################################

def permute_comms(p, tot_lab, kmeans_lab):

    # Create a copy of the labels we will alter
    tot_lab_shuff = copy.deepcopy(tot_lab)

    # Iterate through each class
    for ii in range(2):

        # Grab the indices for this current class
        curr_inds = kmeans_lab['group_inds'][ii]

        # Choose a random percentage of indices
        rand_inds = np.random.choice(curr_inds, 
                                    round(len(curr_inds)*p),
                                    replace = False)

        # Create a copy and shuffle
        rand_inds_shuff = copy.deepcopy(rand_inds)
        np.random.shuffle(rand_inds_shuff)

        # Replace these inds with the shuffled labels
        tot_lab_shuff[rand_inds] = tot_lab[rand_inds_shuff]
        
    return(tot_lab_shuff)


################################################################
# Function to permute classes
################################################################

def permute_class(p, Y, comm_labs = [0]):
    
    # Create copy of Y2
    Y_shuff = copy.deepcopy(Y)
    
    # Create inds
    inds = np.arange(len(Y))
    
    # Choose a random percentage of indices
    rand_inds = np.random.choice(inds, 
                                 round(len(inds)*p),
                                 replace = False)

    # Create a copy and shuffle
    rand_inds_shuff = copy.deepcopy(rand_inds)
    np.random.shuffle(rand_inds_shuff)

    # Replace these inds with the shuffled labels
    Y_shuff[rand_inds] = Y[rand_inds_shuff]
    
    if len(comm_labs) > 0:
        
        # Create copy of comm labels
        comm_labs_shuff = copy.deepcopy(comm_labs)
        
        # Permute the labs from the previous class shuffling
        comm_labs_shuff[rand_inds] = comm_labs[rand_inds_shuff]
        
        return(Y_shuff, comm_labs_shuff)
    
    return(Y_shuff)


################################################################
# Function to permute classes
################################################################

def create_forest(X, Y):
    # Split test and train
    train_x, test_x, train_y, test_y = train_test_split(X, 
                                                        Y, 
                                                        test_size = 0.2, 
                                                        random_state = 42)

    # Create the RF and fit to our data
    rf = RandomForestClassifier(n_estimators = 1000, random_state = 42)
    rf.fit(train_x, train_y);

    # Get the predicted output
    pred_y = rf.predict(test_x)

    # Examine performance metrics
    return(str(round(met.roc_auc_score(test_y, pred_y), 4)))


if __name__ == "__main__":
	pass
else:
	print('Loading functions...\n')
