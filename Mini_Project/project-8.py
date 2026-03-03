import pandas as pd
import os

df=pd.read_csv("/Users/akhmadalievruziboy/Desktop/GitHub/NumPy/Mini_Project/messy_data.csv")

# print(df.info())
# print(df.head())
# print(df.shape)

df.columns=df.columns.str.lower().str.replace(" ","_")
print(df.info())


df['product']=df['product'].fillna("Unknown")

# convert date column to actual datetime objects; keep dtype for later operations
# we avoid overwriting with strings so that dt accessor remains available
# if a string representation is needed (e.g. for export), call dt.strftime when writing

# parse dates; coerce invalid inputs to NaT so dtype becomes datetime64
# 'mixed' is not a valid format string so we rely on pandas' inference
# using errors='coerce' ensures conversion even if some rows are bad

df['date']=pd.to_datetime(df["date"], errors='coerce')

# report dtype after conversion to confirm success
print("after conversion", df['date'].dtype)



df["sales_amount"]=df["sales_amount"].replace(['NULL','N/A','twelve hundred'], None)
df["sales_amount"]=pd.to_numeric(df["sales_amount"], errors='coerce')
df["sales_amount"]=df["sales_amount"].fillna(df["sales_amount"].median()).astype(int)

df['region']=df['region'].str.lower().str.capitalize().str.strip()

df['customer_id']=df["customer_id"].fillna('Unknown').str.strip()

df['quantity']=pd.to_numeric(df["quantity"], errors='coerce')
df["quantity"]=df["quantity"].fillna(1).astype(int)
df["quantity"]=df["quantity"].apply(lambda x: x if x>=0 else 1)

df['payment_method']=df["payment_method"].str.lower().str.capitalize().str.strip()

print("duplicated: ", df.duplicated().sum())

# df.to_csv('Cleaned_sales_data.csv', index=False)

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# plot sales amount over time
plt.plot(df['date'], df['sales_amount'])

# configure formatter to display month as two digits (01, 02, ...)
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m'))

# expand the view to include the very first day of the first month
# (MonthLocator places ticks on the first of each month, so if the
# earliest data point occurs after the 1st the tick is omitted.)
start = df['date'].min().to_period('M').to_timestamp()
end = (df['date'].max().to_period('M') + 1).to_timestamp()
ax.set_xlim(start, end)

# rotate and align date labels nicely
plt.gcf().autofmt_xdate()

plt.title("Sales Amount Over Time", fontsize=14, fontweight='bold', color='blue')
plt.xlabel('Date 2024', fontsize=10, color='green')
plt.ylabel('Sales Amount', fontsize=10, color='green')

# hide manual xticks call since formatter handles month labels
# plt.xticks(df['date'].dt.to_period('M').dropna().unique().to_timestamp(), rotation=45)
plt.tight_layout()

plt.show()