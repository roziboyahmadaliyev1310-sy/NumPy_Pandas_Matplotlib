import pandas as pd

# Dataframe = A tabular data structure with rows AND columns. (two-Dimensional)
# Similar to an Excel spreadsheet

data={"Name":['jhon','ali','smith','jonsen'],
      'Age':[30,45,20,65]}
df=pd.DataFrame(data,index=['employee1','employee2','employee3','employee4'])
print(df,"\n")

# Taking data by location (loc)
print(df.loc['employee3'],"\n")

# Add a new column
df['Job']=['cooker','driver','cashier','sealer']
# taking data by its index
# print(df.iloc[0])

print(df,"\n")

# Add a new row
new_rows=pd.DataFrame([{'Name': 'Sandy', 'Age':20,'Job':'builder'},
                       {'Name': 'mike', 'Age':34,'Job':'businessmen'}],
                     index=['employee5','employee6'])
df=pd.concat([df,new_rows])

print(df)