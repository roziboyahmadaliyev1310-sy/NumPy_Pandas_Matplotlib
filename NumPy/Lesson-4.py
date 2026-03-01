import numpy as np

# slicing of array ✂
array=np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])
# array[start:end:step]
print(array[0],"\n")
print(array[1:3],"\n")
print(array[0:4:2],"\n")

# slicing of array in reverse order
print(array[::-1],"\n")

# slicing of array vertically
print(array[1:,2])


