---
layout: post
title: 	Synthetic Data with Sklearn
categories: blog
date: 2019-10-31
published: true
share: true
image:
  feature: omniglot_header_dark.jpg
tags: [synthetic data, sklearn, data synthesis, algorithm validation]
---

# Synthetic Data Generation 

We are going to be using **sklearns** function ```python dataset.make_classification()``` to create synthetic datasets. We can specifiy arguments to specify the number of *informative, redundant,* and *repeated* features in the dataset. Synthetic data can be great as we can control every aspect of our data including the *number of classes, features (informative, redundant, repeating, noise), clusters within each class, and the separation of these clusters*.

**There are many opportunities to examine...**

* How an increasing number of noisy features affects classification performance
* Performance of community detection and clustering algorithms with varying levels of class separability
* How varying dimensionality alters runtime of new algorithms

For the sake of this demonstration we are going to focus on this bit; **Performance of community detection and clustering algorithms with varying levels of class separability**

**Primary Goals**

- Two class labels with varying class separability
- Four clusters per class
- Varying levels of cluster separation

### Class Separation

- Let's, examine how the class_sep looks within the data  
- We will only select to create 3 features to better visualize the class separation. However, one can imagine that 


```python

import numpy as np

# Modified sklearn function to 
	# To output the cluster label of every observation
from sklearn.datasets import sample_gen_gh as gh
import matplotlib.pyplot as plt

# Iterate through varying class_sep
for sep_val in np.arange(.75, 4.75, 1.0):

	# Create data
	X, Y, clust = make_classification(n_samples=1000,
		n_features=3,
		n_informative=3,
		n_redundant=0,
		n_repeated=0,
		n_classes=2,
		n_clusters_per_class=4,
		class_sep = sep_val,
		shuffle = False)

	# Custom function to write plot output
	write_3d_plot(X, Y)

```

![](/images/blogs/data_synth/plot_sep.png)

We are going to be examining a new algorithm developed by Feczko et al 2018 [Functional Random Forest](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30092-0). In the case of a binary classification problem, the algorithm builds a random forest to classify a specified training portion of the data, after which it creates a proximity matrix from the structure of said forest where each node represents an observation and every edge denotes the number of times two observations found themselves in the same terminal node from the random forest. From this point, one can identify community substructure using community detection methods, in the case of the FRF, infomap community detection. 

We are going to try and use synthetic data, with known community class community structure to identify the algorithms ability to capture the "ground truth" community labels.

