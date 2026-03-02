import kagglehub
import os
import pandas as pd

path=kagglehub.dataset_download("ashyou09/samsung-global-product-sales-dataset")

# for file in os.listdir(path):
#         print(file)

df=pd.read_csv(os.path.join(path,"samsung_global_sales_dataset.csv"))

# print(df.head())
# print(df.shape)



# print(df.isna().sum())
df['storage']=df["storage"].fillna('Unknown')
df['previous_device_os']=df['previous_device_os'].fillna("unknown")
df['customer_rating']=df['customer_rating'].fillna(df['customer_rating'].mean())

# print("duplicated: ",df.duplicated().sum())

df['sale_date']=pd.to_datetime(df['sale_date'])
# print(df.dtypes)

# Unique qiymatlarni tekshirish
print("return_status:", df['return_status'].unique())
print("is_5g:", df['is_5g'].unique())
print("sales_channel:", df['sales_channel'].unique())
print("payment_method:", df['payment_method'].unique())
print("customer_segment:", df['customer_segment'].unique())
print("previous_device_os:", df['previous_device_os'].unique())

print(df[['unit_price_usd', 'discount_pct', 
          'units_sold', 'customer_rating', 
          'revenue_usd']].describe())