import matplotlib.pyplot as plt
import numpy as np

# Histogram = A visual representation of the distribution of quantiyayive data.
#             They group values into bins (intervals)
#              And counts how many fall in each range

scores=np.random.normal(loc=70,scale=10,size=100)
scores=np.clip(scores,0,100)

plt.hist(scores, bins=10,
                 color='green',
                 edgecolor='black')

plt.title("Test scores")

plt.xlabel("Score")
plt.ylabel('Number of students')

plt.show()