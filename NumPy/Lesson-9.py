import numpy as np

# seed is used to generate the same random numbers every time we run the code
rng=np.random.default_rng()

print(rng.integers(low=1,high=30,size=(3,2)))

# uniform distribution
print(np.random.uniform(1,15,size=2),"\n")

# shuffle the array
array=np.array([1,2,3,4,5,6,7,8,9,10])
rng.shuffle(array)
print(array,"\n")

# choice is used to randomly select elements from an array

choices=np.array(['apple','banana','cherry','pineapple'])
fruit=rng.choice(choices,size=(2,3))
print(fruit)