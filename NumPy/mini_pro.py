import numpy as np

# Finding the mean, median, standard deviation(std), variance(var) 
# and percentile of the given score using numpy functions

class MiniPro:
    def __init__(self,scores):
        self.score=np.array(scores)

    def project(self):
        print(np.mean(self.score),"\n")
        print(np.median(self.score),"\n")
        print(np.std(self.score),"\n")
        print(np.var(self.score),"\n")
        print(np.percentile(self.score,50),"\n")

scores=[80,90,100,45,67,78,88]
MiniPro(scores).project()