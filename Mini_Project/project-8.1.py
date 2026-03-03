import pandas as pd
import os

df=pd.read_csv("/Users/akhmadalievruziboy/Desktop/GitHub/NumPy/Mini_Project/employee_data_messy.csv")

# print(df.shape)
# print(df.head())
# print(df.info())

df.columns=df.columns.str.lower().str.replace(" ","_").str.strip()


df['name']=df["name"].fillna('Unknown').str.strip()

df['salary']=df['salary'].replace('seven thousand', '7000').replace(['NULL', 'N/A'], None)
df['salary']=pd.to_numeric(df['salary'], errors='coerce')
df['salary']=df['salary'].fillna(df['salary'].median(), inplace=True).astype(int)


df['performance_rating']=df['performance_rating'].fillna(df['performance_rating'].median(), inplace=False).astype(float)

df['department']=df['department'].str.lower().str.title().str.strip()

df['city']=df['city'].str.lower().str.title().str.strip()


df_cleaned=df.copy()

df_cleaned.to_csv('Cleaned_employee_data.csv', index=False)