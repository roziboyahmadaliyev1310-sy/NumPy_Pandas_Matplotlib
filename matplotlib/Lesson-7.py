import matplotlib.pyplot as plt
import numpy as np

# Scatter graph = shows the relationship between two varibales 
#                  Helps to identify a correlation (+,-,None)
#                  Example: study hours vs. test scores

x=np.array([2,3,4,5,5,6,8,7,5,8])
y=np.array([50,55,60,65,70,75,80,85,90,95])

x1=np.array([0,4,5,5,6,7,8,8,8,7])
y1=np.array([45,52,57,68,73,78,87,92,97,98])

plt.scatter(x,y,color='blue',
                s=170,
                alpha=0.5,
                label="Class A")

plt.scatter(x1,y1,color='red',
                s=170,
                alpha=0.5,
                label="Class B")

plt.title("Test score",color='skyblue',
                        fontsize=25,
                        fontweight='bold')
plt.xlabel("Hours studied", color='red',
                            fontsize=20,
                            family='Arial',
                            fontweight='bold')

plt.ylabel("Grade", color='red',
                    fontsize=20,
                    family='Arial',
                    fontweight='bold')

plt.legend()
plt.show()