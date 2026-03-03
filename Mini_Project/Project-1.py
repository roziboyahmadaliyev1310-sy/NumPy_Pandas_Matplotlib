import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

import kagglehub

# Download latest version
path = kagglehub.dataset_download("ashyou09/apple-global-product-sales-dataset")

df=pd.read_csv(os.path.join(path,'apple_global_sales_dataset.csv'))

df.columns=df.columns.str.lower().str.replace(" ","_")
df=df.drop_duplicates()

df['sale_date']=pd.to_datetime(df['sale_date'])

avg_figure=df.groupby('year')['customer_rating'].mean()

plt.figure(figsize=(10,5))
plt.plot(avg_figure.index, avg_figure.values)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()