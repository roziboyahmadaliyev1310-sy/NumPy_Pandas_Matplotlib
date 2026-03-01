import numpy as np

# array dimension
# Zero-dimensional array
array=np.array('A')

# checking the dimension of array using ndim--number of dimensions
print(array.ndim,"\n")

#one-dimensional array
one_d_array=np.array(['a','b','c','d'])
print(one_d_array.ndim,"\n")

# two-dimensional array
two_d_array=np.array([['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l']])
print(two_d_array.ndim,"\n")

# three-dimensional array
three_d_array=np.array([[['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l']],
                      [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l']],
                      [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l']]])
print(three_d_array.ndim,"\n")

# array shape
print(array.shape,"\n")
print(one_d_array.shape,"\n")
print(two_d_array.shape,"\n")
print(three_d_array.shape)

# number of pages
# number of lines on each page
# number of elements on each line