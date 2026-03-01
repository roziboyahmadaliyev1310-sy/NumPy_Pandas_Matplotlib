import matplotlib.pyplot as plt
import numpy as np

# PIE chart = Circular chart divided into slices to show percentage of the total.
#             Good for Visualizing distribution among categories.

IELTS_takers=np.array(['Uzbekistan', 'Kazakistan', 'Tajikistan', 'Kirgizistan'])
grades=np.array([7000,5900,2978,2130])
colors=['red','yellow','orange','green']
plt.pie(grades, labels=IELTS_takers,
                autopct="%1.1f",
                colors=colors,
                explode=[0,0,0.1,0],
                shadow=True,
                startangle=90)

plt.title('IELTS Taking numbers',
          fontsize=20,
          family="Arial",
          fontweight="bold",
          color='#2765c2')

plt.xlabel('Countries',
           fontsize=20,
          family="Arial",
          fontweight="bold",
          color='#2765c2')

plt.show()