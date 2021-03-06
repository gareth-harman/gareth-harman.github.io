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

We are going to be using **sklearn**'s function `datasets.make_classification()` to create synthetic datasets. We can specifiy arguments to specify the number of *informative, redundant,* and *repeated* features in the dataset. Synthetic data can be great as we can control every aspect of our data including the *number of classes, features (informative, redundant, repeating, noise), clusters within each class, and the separation of these clusters*.

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

- Let's, examine how the class_sep affects the data   
- We will only engineer 3 features to better visualize the class separation 


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

## Visualizing relationships within the data

It can be difficult to try and identify underlying structure within a dataset with many many features. However, there are a few methods that might help, first we will try `hierarchical clustering`, `PCA`, and finally `TSNE`.

We will further be dilineating how class separation alters the underlying structure as well.

**Class sep 1.5**

![](/images/blogs/data_synth/clustering_1_5.png)

**Class sep 2.5**

![](/images/blogs/data_synth/clustering_2_5.png)

**Class sep 3.5**

![](/images/blogs/data_synth/clustering_3_5.png)




