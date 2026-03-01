import numpy as np

# scalar arithmetic

array=np.array([1,2,2,3,4])

print(array+10,"\n")
print(array-2,"\n")
print(array*2,"\n")
print(array/2,"\n")
print(array**4,"\n")
print(array%2!=0,"\n")





# Vectorized mathematical functions
array1=np.array([4,9,16,25])

# Square root of array 
print(np.sqrt(array1),"\n")

# finding radius
print(np.pi*array1**2)

# round off the value of pi, array
round_pi=np.round(np.pi,2)
print(round_pi)

# ceiling and floor of array
ceil_floor_array=np.array([1.34,2.98,98.01])
print(np.floor(ceil_floor_array),"\n")
print(np.ceil(ceil_floor_array),"\n")




# Element-wise operations
array2=np.array([1,2,3,4])
array3=np.array([10,11,12,13])

# adding, subtracting, multiplying, dividing two arrays vertically
print(array2+array3,"\n")
print(array2-array3,"\n")
print(array2*array3,"\n")
print(array2/array3,"\n")




# comparing two arrays 
array2=np.array([1,2,3,4])
array3=np.array([10,11,12,13])

print(array2==array3,"\n")
print(array2<array3,"\n")
print(array2>array3)



