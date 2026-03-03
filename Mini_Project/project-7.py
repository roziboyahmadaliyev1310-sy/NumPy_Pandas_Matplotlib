import kagglehub
import os
# Download latest version
path = kagglehub.dataset_download("thedevastator/uncovering-global-data-professional-salary-trend")
# for file in os.listdir(path):
#     print(os.path.join( file))



import pandas as pd

df=pd.read_csv(os.path.join(path,'2019_Data_Professional_Salary_Survey_Responses.csv'))

# print(df.shape)
# print(df.info())
# print(df.describe())

for col in df.columns:
    if df[col].isna().sum()>0:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col]=df[col].fillna(df[col].mean())
        else:
            df[col]=df[col].fillna("Unknown")

# print(df.isna().sum())

df.columns=df.columns.str.lower().str.replace(":" ,"").str.replace(" ","_")
# print(df.info())

print("duplicated :", df.duplicated().sum())

