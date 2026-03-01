import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
# print(df)

# FILTERING WITH GROUPBY()

group=df.groupby('Pclass')

print(group['Fare'].max())
print(group['Fare'].min())
print(group['Fare'].sum())
print(group['Fare'].mean())


