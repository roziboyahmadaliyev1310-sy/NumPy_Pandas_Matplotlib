import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

import kagglehub

# Download latest version
path = kagglehub.dataset_download("mhassansaboor/bmw-stock-data-1996-2024")

# print("Path to dataset files:", path)

df=pd.read_csv(os.path.join(path, 'BMW_stock_data.csv'))

print(df)
# # Convert Date column to datetime
# df['Date'] = pd.to_datetime(df['Date'])
# plt.plot(df['Date'],df['Close'])

# plt.title("BMW Stock Price 1996-2026",color='red',
#                                       fontsize=25,
#                                       fontweight='bold')
# plt.xlabel("Date", color='skyblue',
#                    fontweight='bold',
#                    fontsize=20)
# plt.ylabel("Close",color='skyblue',
#                    fontweight='bold',
#                    fontsize=20)
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()