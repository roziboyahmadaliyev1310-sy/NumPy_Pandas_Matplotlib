import pandas as pd

# Aggregate functions= Reduce a set of values into a single summary value
#                     used to summarize and analyze data, often used with groupby() function


df=pd.read_csv("CityTable.csv")

# whole DataFrame
print(df.mean(numeric_only=True),"\n")
print(df.max(numeric_only=True),"\n")
print(df.median(numeric_only=True),"\n")
print(df.min(numeric_only=True),"\n")
print(df.sum(numeric_only=True),"\n")
print(df.std(numeric_only=True),"\n")
print(df.count())

# Single DataFrame
print(df['population'].mean())
print(df['population'].max())
print(df['population'].min())
print(df['population'].count())

