from random import choice
import matplotlib.pyplot as plt
import scipy.stats as st
import seaborn as sns
import numpy as np

if 'd' not in locals():
    d = [4, 10, 1 , 3, 2]
    
meanss =[] 

for ii in range(0, 50000):
    e = [choice(d), choice(d), choice(d), choice(d), choice(d)]
    temp_me = sum(e)/len(e)
    meanss.append(temp_me)

n_perc = int(len(meanss) * .05)
f_sort = sorted(meanss)

low = sum(f_sort[:n_perc]) / len(f_sort[:n_perc])
high = sum(f_sort[-n_perc:]) / len(f_sort[-n_perc:])

#plt.hist(meanss, color='green', histtype='stepfilled', facecolor='g', alpha=.5)

sns.distplot(meanss, color='green')
plt.ylabel('Occur')
plt.xlabel(r'$\sum_{i=0}^\infty x_i$')
plt.axvline(x = low, color = 'r', linestyle = '--')
plt.axvline(x = high, color = 'r', linestyle = '--')
plt.yticks(np.arange(0, .5, .1))
sns.bootstrap()

#plt.axvline(x=low, color='r', linestyle='--')
#plt.axvline(x=high, color='r', linestyle='--')
#plt.axvline(x=sum(meanss)/len(meanss), color='blue', linestyle='-')
#
#plt.xlabel(r'$\sum_{i=0}^\infty x_i$')
#plt.ylabel('Occur')
