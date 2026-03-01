import pandas as pd
import os

df=pd.read_csv("/Users/akhmadalievruziboy/Desktop/GitHub/NumPy/Mini_Project/dirty_cars_data.csv")
print(df.head())
# print(df.shape)
print(df.info())

df.columns=df.columns.str.lower().str.replace(" ","_")

print(df.isna().sum())

df['engine_size']=df['engine_size'].fillna(0)
for col in df.columns:
    if df[col].isna().sum()>0:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col]=df[col].fillna(df[col].mean())
        else:
            df[col]=df[col].fillna("Unknown")

print(df.isna().sum())

print("duplicated befor :",df.duplicated().sum())
df=df.drop_duplicates()

print("duplicated after: ",df.duplicated().sum())
df.to_csv("cleaned_cars_data.csv", index=False)