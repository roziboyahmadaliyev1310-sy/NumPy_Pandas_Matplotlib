import numpy as np

# taking with index of array
# multidimensional array 
array=np.array([[['a','b','c'],['d','e','f'],['g','h','i']],
                [['j','k','l'],['m','n','o'],['p','q','r']],
                [['s','t','u'],['v','w','x'],['y','z','']]])
print(array[0,1,2])

# making a list of 3 pages, each page has 2 lines and each line has 4 elements
# making a birthday by using array number
name=array[1,2,2]+array[1,1,2]+array[2,2,1]+array[0,2,2]+array[0,0,1]+array[1,1,2]+array[2,2,0]
print(name)