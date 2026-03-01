import pandas as pd
df = pd.read_csv("/Users/akhmadalievruziboy/Desktop/GitHub/NumPy/Pandas/US_Top_50_Universities_2026.csv")

# 1. Drop irrelevent columns
df=df.drop(columns=['PassengerId','Survived','Embarked'])

# 2. Handle missing value
df=df.dropna(subset=['Cabin'])

# fillna = is used to change NaN
df=df.fillna({'Cabin': 'NoNe'})


# print(df)

# 3. Fix inconsistent values
df['Institution_Type']=df['Institution_Type'].replace({'Private': 'PRIVATE',
                                                       'Public':'PUBLIC'})
print(df.to_string())


# 4. STANDARDIZE TEXT

df['University_Name']=df['University_Name'].str.lower()
print(df)