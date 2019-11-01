---
layout: post
title: Adaptive Optics
categories: blog
date: 2019-11-01
published: true
share: true
image:
  feature: my_ao_filt.png
tags: [adaptive optics, retinal, retinal imaging, algorithms]
---

## Novel Algorithms for Adaptive Optics

Adaptive optics is an imaging modality designed by NASA to track russian satellites during the Cold War. It is an optical system that detects and corrects for aberrations in the wavefront using a deformable mirror situated atop a matrix of actuators. The system can correct for motion artifact. In the case of imaging satellites, the target is large and the path length is quite long, however, this problem has been recast to imaging photoreceptors in the back of the eye in the retina. The eye is in constant motion, these rapid movements make imaging at the cellular level especially difficult despite having a very short path length. See below for a figure from [Gill Et Al. 2019 Cellular imaging of inherited retinal diseases using adaptive optics](https://www.nature.com/articles/s41433-019-0474-3) describing the optical system.

![](/images/blogs/novel_algorithms/ao_system.png)

## Overview

- Essentially, we want to identify a new metric that helps to validate cones identified by automated cone detection algorithms are stable across imaging sessions
- 

### Cone Location Similarity Algorithm

\\(C_i\\) is a matrix containing the pixel coordinates for each of the n cones from image \\(i\\).

$$
C_{i}=\left[\begin{array}{c}{\left(x_{1}, y_{1}\right)} \\ {\cdots} \\ {\left(x_{n}, y_{n}\right)}\end{array}\right]
$$

We can represent pixel coordinates \\((x_1, y_1)\\) for the first cone in set \\(C_i\\) as \\(c_1\\) and declare the Euclidean distance between coordinates \\(c_1\\) and \\(c_2\\) as...

$$
|c_{1}, c_{2}|^{2}
$$

And,

$$
\left(x_{1}-x_{2}\right)^{2}+\left(y_{1}-y_{2}\right)^{2}=\left\|c_{1}, c_{2}\right\|^{2}
$$

We then create a vector of distances between cone \\(c_i\\) of set \\(C_i\\) and all of the cones \\((x)\\) for each of our images \\(N\\)

$$
X_{i}=\left\|c_{i}, x\right\|^{2}: x \in C_{N}
$$

\\(c_i\\) is said to be a shared cone if there exists a cone within the declared distance threshold \\(t\\), 5 pixels, of all other sets of images

$$
f(x)=\left\{\begin{array}{ll}{1,} & {\text { if } \min \left(X_{i}\right) \leq t: \text { for all } \mathrm{N} \text { sessions }} \\ {0,} & {\text { else }}\end{array}\right.
$$

In the case that multiple cones exist within our threshold of \\(c_i\\), the cone is chosen that will minimize the mean distance between cones from all images \\(N\\)

$$
arg \min \frac{1}{N} \sum_{i=1}^{N} \sum_{j=1}^{N-1}\left\|c_{i}, c_{j}\right\|^{2}
$$

Finally, cone location similarity is reported as the percentage of the number of detected shared cones, \\(C_s\\), and the mean number of cones, detected across \\(N\\) imaging sessions, where \\(n_s\\) is the number of cones detected

$$
C L S=\frac{C_{s}}{\frac{1}{N} \sum_{i=1}^{N} n_{c}} \times 100
$$


![](/images/novel_algorithms__new_overview.png)

- More text down here

