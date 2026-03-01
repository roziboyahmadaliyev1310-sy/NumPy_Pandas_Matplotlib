import numpy as np

# Filtering= Refers to the process of selecting elements 
# from an array that math a given condition

ages=np.array([[10,20,23,34,54,67],
               [12,45,65,23,32,18]])
# filtering ages lower than 18
teenagers=ages[ages<=18]
print(teenagers,"\n")

# filtering ages between 18 and 40
adults=ages[(ages>18) & (ages<40)]
print(adults,"\n")

# filtering ages greater than 40
seniors=ages[ages>=40]
print(seniors,"\n")

# evens and odds numbers
evens=ages[ages%2==0]
odds=ages[ages%2!=0]
print(evens,"\n")
print(odds,"\n")


# where function
# np.where(condition, x, y) returns an array with elements from x where the condition
# is true and elements from y where the condition is false

adults1=np.where((ages>18) & (ages<40), ages, 0)
print(adults1)