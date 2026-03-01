import matplotlib.pyplot as plt
import numpy as np

# Bar chart = compare categories of data by representing each category with a bar

TV_show=np.array(["Milliy TV", "ZO`R TV", 'Footbal TV','MY5','Bolajon'])
value=np.array([1139,2350,978,1500,540])

plt.bar(TV_show,value)

plt.title("Daily waching TV shows",
          fontsize=20,
          family='Arial',
          fontweight='bold',
          color='#279bc2')

plt.xlabel('TV shows',
           fontsize=20,
          family='Arial',
          fontweight='bold',
          color='#279bc2')

plt.ylabel('Live waching',
           fontsize=20,
          family='Arial',
          fontweight='bold',
          color='#279bc2')

plt.show()