import matplotlib.pyplot as plt
import numpy as np

# GRID() = Helps make plots easier to read by adding reference lines.

x=np.array([1,2,3,4,5])
y=np.array([5,10,15,20,25])

plt.grid(axis='y',
         linewidth=2,
         color='lightgray',
         linestyle='dashed')

plt.plot(x,y)

plt.show()