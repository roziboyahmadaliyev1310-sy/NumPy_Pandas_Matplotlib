import pandas as pd
import os

df = pd.read_csv("/Users/akhmadalievruziboy/Desktop/GitHub/NumPy/Mini_Project/cars_data_1.csv")
# print(df.head())
# print(df.shape)
print(df.info())

df.columns=df.columns.str.lower().str.replace(" ","_")
# print(df)


# print(df.isna().sum().sum())

# df.fillna(df.mean(numeric_only=True), inplace=True)
# df.fillna('Unknown', inplace=(True))
df['engine_size']=df["engine_size"].fillna(0)

for col in df.columns:
    if df[col].isna().sum()>0:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col]=df[col].fillna(df[col].mean())
        else:
            df[col]=df[col].fillna('Unknown')

# print(df.isna().sum())

# print("duplicated: ",df.duplicated().sum())

df.to_csv('cars_cleaned.csv', index=False)
