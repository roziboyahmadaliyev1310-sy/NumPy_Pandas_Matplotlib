import pandas as pd

df=pd.read_csv("CityTable.csv")

# high_population=df[df['population']>2900000]

# print(high_population)
high_population=df[df['population']>2900000]

print(high_population)