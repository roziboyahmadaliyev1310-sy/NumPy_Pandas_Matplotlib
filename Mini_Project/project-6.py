import pandas as pd
import os
import re


df=pd.read_csv("/Users/akhmadalievruziboy/Desktop/GitHub/NumPy/Mini_Project/messy_customer_data.csv")

# print(df.info())

df.columns=df.columns.str.lower().str.replace(" ","_")
# print(df.info())


# print(df["registration_date"].dtype)
df['registration_date']=df["registration_date"].str.replace("/","-")

df["registration_date"]=pd.to_datetime(df["registration_date"], format='mixed')

# print(df['registration_date'])
# print(df.describe())
# print(df.isna().sum())
df['phone_number']=df["phone_number"].replace('nan','')
df['phone_number']=df['phone_number'].replace('invalid phone','')

def clean_phone_number(phone):
    phone=str(phone)

    if phone in [' ','nan','None','NULL','invalid phone']:
        return None
    digits=re.sub(r'\D','',phone)

    if len(digits) == 7:
        return f"{digits[:3]}-{digits[3:]}"
    elif len(digits)==10:
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    else:
        return None
    
df['phone_number']=df['phone_number'].apply(clean_phone_number)

df['age']=df['age'].fillna(df['age'].median())
df['phone_number']=df['phone_number'].fillna('Not Provided')
df['first_name']=df['first_name'].fillna('Unknown')
df['purchase_amount']=df['purchase_amount'].fillna(0)

df['loyalty_status']=df['loyalty_status'].str.lower().str.capitalize()

df.loc[df['age'] < 0,'age']=df['age'].median()
df.loc[df['age'] < 120,'age']=df['age'].median()

df.loc[df['annual_income']<=0,'annual_income']=df['annual_income'].median()

df['email']=df['email'].str.lower().str.strip()

df['first_name']=df['first_name'].str.strip()
df['last_name']=df['last_name'].str.strip()
# print('before',df.duplicated().sum())
df=df.drop_duplicates()

# df.to_csv('/Users/akhmadalievruziboy/Desktop/GitHub/NumPy/Mini_Project/cleaned_customer_data.csv', index=False)


print(df.to_string())