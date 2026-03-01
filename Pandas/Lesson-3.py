import pandas as pd

# CALLING INDEX WITH NAME
df=pd.read_csv('CityTable.csv',index_col="name")
# print(df)

# Selection by column/s
# print(df['name'])
# print(df['country_code'])
# print(df[['id','name','population']])

# SELECTION ROW/S
# print(df.loc[100])
# print(df.iloc[1])


country_name=input('Enter a country to know about ')

try:
    print(df.loc[country_name])
except KeyError:
    print(f"{country_name} not found")

