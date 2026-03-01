import matplotlib.pyplot as plt
import numpy as np
x=np.array([2023,2024,2025,2026])
y=np.array([10.2,15.0,14.7,18.0])
y1=np.array([14.10,11.7,13.9,20.4])
y2=np.array([15,14,15,17])

line_style=dict(marker='.',
                markersize=20,
                markerfacecolor='#1cd3fc',
                markeredgecolor='#1cd3fc',
                linestyle='dashdot',
                linewidth=4)


plt.plot(x,y,color='green',**line_style)
plt.plot(x,y1,color='yellow',**line_style)
plt.plot(x,y2,color='black',**line_style)

plt.title('BORNING RATE')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()
plt.show()