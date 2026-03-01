# import matplotlib
import matplotlib.pyplot as plt


# print(matplotlib.__version__) 

x=[2020,2021,2022,2023,2024,2025]
y=[10,50,70,80,65,86]

plt.plot(x,y)
plt.title("MY first chart")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()