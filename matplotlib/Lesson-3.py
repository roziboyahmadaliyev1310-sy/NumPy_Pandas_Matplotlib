import matplotlib.pyplot as plt
import numpy as np

# labels with matplotlib.pyplot

x=np.array([2023,2024,2025,2026])
y1=np.array([15,20,25,19])
y2=np.array([12,25,20,20])
y3=np.array([20,14,18,25])

plt.title('Transport Payment',fontsize=25,
                              family='Arial',
                              fontweight='bold',
                              color='#4e8bf5')

plt.xlabel("Year",fontsize=20,
                  family='Arial',
                  fontweight='bold',
                  color='#2dbefc')

plt.ylabel("WON",fontsize=20,
                 family='Arial',
                 fontweight='bold',
                 color="#2dbefc")

# tick_params - is used to give collor to number that in X or Y, 'Both' label
plt.tick_params(axis='both',
                colors='#2dbefc')

plt.plot(x,y1,color='#306bc9')
plt.plot(x,y2,color='#30bac9')
plt.plot(x,y3,color='#a2cf42')

#  plt.xticks() - is used to write only we given number/ it will show number in the graph
#                     that we write in array
plt.xticks(x)

plt.show()