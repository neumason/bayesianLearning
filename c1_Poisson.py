import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
figsize(12.5,4)
a = np.arange(16)
print a
p = stats.poisson
# print dir(p)
l = [1.5,4.25]
colors = ['#348ABD','#A60628']

plt.bar(a,p.pmf(a,l[0]),color =colors[0],label='$\lambda=%.1f$'%l[0],alpha=0.60,edgecolor=colors[0],lw='3')
print p.pmf(a,l[0])
plt.bar(a,p.pmf(a,l[1]),color =colors[1],label='$\lambda=%.1f$'%l[1],alpha=0.60,edgecolor=colors[1],lw='3')
plt.xticks(a+0.4,a)
plt.legend()
plt.ylabel('probability of $k$')
plt.xlabel('$k$')

plt.show()