import numpy as np

# Aggregate functions=summarize the data and typially 
# return a single value     

array=np.array([[1,2,3,4],
                [5,6,7,8]])

# sum of all the elements in the array
print(np.sum(array),"\n")

print(np.mean(array),"\n")
print(np.median(array),"\n")
print(np.std(array),"\n")
print(np.var(array),"\n")
print(np.min(array),"\n")
print(np.max(array),"\n")
print(np.argmax(array),"\n")
print(np.argmin(array),"\n")

print(np.sum(array,axis=1))