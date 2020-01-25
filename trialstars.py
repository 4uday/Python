import matplotlib.pyplot as plt

import numpy as np

x=[1,2,3,4,5,6,7,8,9,10]
y=[2,5,1,6,4,3,9,2.1,2.5,4.5]
plt.scatter(x,y, label='stars', color='y', marker = '*', s=30)
plt.xlabel=('x-axis')
plt.ylabel=('y-axis')
plt.legend()
plt.show()
