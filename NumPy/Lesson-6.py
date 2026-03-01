import numpy as np

# Broadcasting allows us to perform operations on arrays of different 
# shapes and sizes without explicitly reshaping them.

# It automatically applies the operation to each element of the smaller 
# array across the larger array.

# the dimensions have the same size 
# Or one of the dimensions is of size 1

array1=np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])
array2=np.array([[1],[2],[3],[4]])

print(array1.shape,"\n")
print(array2.shape,"\n")

# multipling two arrays of different shapes using broadcasting
result=array1*array2
print(result)