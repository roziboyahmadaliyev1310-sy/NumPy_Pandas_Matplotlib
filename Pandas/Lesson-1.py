import pandas as pd

# print(pd.__version__)

# A Series = A Pandas One-Dimensional labeled array that can hold any data type 
#    Think of it like a single column in a spreadsheet (One-Dimensional)

# Data type would change according to given varibale data
# data=[100.1,104.2,105.3]

data=[100,104,105]


series=pd.Series(data, index=('a','b','c'))
print(series,"\n")

# useing loc to take data according to lable location
# and even we could change the data by using loc

series.loc['a'] = 200
print(series,"\n")

# iloc is used to take data by index
print(series.iloc[2],"\n")

# Filtering data
data1=[150,201,200,198,149]

serie=pd.Series(data1,index=['a','b','c','d','e'])
print(serie[serie>=200],"\n")


study_hours={'Day1':4,
             'Day2':3,
             'Day3':5,
             'Day4':4}

series1=pd.Series(study_hours)
print(series1[series1!=4])