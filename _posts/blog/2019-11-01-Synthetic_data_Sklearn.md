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

We are going to be using `sklearns.dataset` function `make_classification()` to create synthetic datasets. 

**Primary Goals**

- Two class labels with varying class separability
- Four clusters per class
- Varying levels of cluster separation

```python

import numpy as np
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

	write_3d_plot(X, Y)

```
### Class Separation

Let's, examine how the class_sep looks within the data

![](/images/blogs/data_synth/plot_sep.png)