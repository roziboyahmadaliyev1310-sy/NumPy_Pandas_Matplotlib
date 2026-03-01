import pandas as pd
import kagglehub
import os

path=kagglehub.dataset_download("sandhyakrishnan02/world-population-19512020")
# for file in os.listdir(path):
#     print(file)

df=pd.read_csv(os.path.join(path,"World Population Projections(2020-2100).csv"))


print(df.shape)

# print(df.isna().sum())
# print("duplicated: ",df.duplicated())
df.columns=df.columns.str.lower().str.replace(" ","_")
print(df.head())
print(df.to_string())