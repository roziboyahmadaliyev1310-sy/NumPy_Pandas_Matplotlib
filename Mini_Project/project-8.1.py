import pandas as pd
import os

print('='*70)
print("malumotlarni tozalash v analiz qilish")
print('='*70)

df=pd.read_csv("/Users/akhmadalievruziboy/Desktop/GitHub/NumPy/Mini_Project/employee_data_messy.csv")

# print(df.shape)
# print(df.head())
# print(df.info())

df.columns=df.columns.str.lower().str.replace(" ","_").str.strip()


df['name']=df["name"].fillna('Unknown').str.strip()

df['salary']=df['salary'].replace('seven thousand', '7000').replace(['NULL', 'N/A'], None)
df['salary']=pd.to_numeric(df['salary'], errors='coerce')
df['salary']=df['salary'].fillna(df['salary'].median()).astype(int)

df['age']=pd.to_numeric(df['age'], errors='coerce')
df.loc[(df['age']<=0) | (df['age'] > 100), 'age']=df['age'].median()
df['age'].fillna(df['age'].median())  
df['age']=df['age'].astype(int)



df['performance_rating']=df['performance_rating'].fillna(df['performance_rating'].median()).astype(int)

df['department']=df['department'].str.lower().str.title().str.strip()
special_cases = ['IT', 'HR', 'AI', 'ML', 'CEO', 'CTO', 'CFO']
for case in special_cases:
        df['department'] = df['department'].str.replace(case.lower(), case, case=False)



df['city']=df['city'].str.lower().str.title().str.strip()


# Join_Date ni tozalash
df['join_date']=pd.to_datetime(df['join_date'], format='mixed')
df['join_year']=df['join_date'].dt.year
df['join_month']=df['join_date'].dt.month
# print(df.head())
df_cleaned=df.copy()
df.drop_duplicates(inplace=True)
print('='*75)
print("data cleaned successfully and ready for visualization")
print('='*75)
# df_cleaned.to_csv('Cleaned_employee_data.csv', index=False)


import matplotlib.pyplot as plt
import seaborn as sns


# department bo'yicha o'rtacha ish haqini hisoblash
fig=plt.figure(figsize=(20,10))

plt.subplot(3,3,1)
dept_salary=df.groupby('department')['salary'].mean().sort_values(ascending=False)
sns.barplot(x=dept_salary.index, y=dept_salary.values, palette='viridis')
plt.title('O\'rtacha Maosh - Departmentlar Bo\'yicha', fontsize=14, fontweight='bold')
plt.xlabel('Department', fontsize=11)
plt.ylabel('O\'rtacha Maosh ($)', fontsize=11)
plt.xticks(rotation=45)
for i, v in enumerate(dept_salary.values):
    plt.text(i, v + 500, f'${v:,.0f}', ha='center', fontsize=9)

plt.subplot(3, 3, 2)
city_counts = df['city'].value_counts()
colors = sns.color_palette('pastel')[0:len(city_counts)]
plt.pie(city_counts.values, labels=city_counts.index, autopct='%1.1f%%', 
        colors=colors, startangle=90)
plt.title('Xodimlar Taqsimoti - Shaharlar Bo\'yicha', fontsize=14, fontweight='bold')


plt.subplot(3, 3, 3)
sns.histplot(df['age'], bins=15, kde=True, color='skyblue', edgecolor='black')
plt.title('Yosh Taqsimoti', fontsize=14, fontweight='bold')
plt.xlabel('Yosh', fontsize=11)
plt.ylabel('Xodimlar Soni', fontsize=11)
plt.axvline(df['age'].mean(), color='red', linestyle='--', linewidth=2, 
            label=f'O\'rtacha: {df["age"].mean():.1f}')
plt.legend()

plt.subplot(3, 3, 4)
sns.boxplot(data=df, x='department', y='salary', palette='Set2')
plt.title('Maosh Taqsimoti - Departmentlar Bo\'yicha', fontsize=14, fontweight='bold')
plt.xlabel('Department', fontsize=11)
plt.ylabel('Maosh ($)', fontsize=11)
plt.xticks(rotation=45)

plt.subplot(3, 3, 5)
hire_trend = df.groupby('join_date').size().resample('M').sum()
sns.lineplot(data=hire_trend, marker='o', linewidth=2, markersize=6, color='green')
plt.title('Ishga Qabul Qilish Tendensiyasi (Oylik)', fontsize=14, fontweight='bold')
plt.xlabel('Sana', fontsize=11)
plt.ylabel('Yangi Xodimlar', fontsize=11)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

plt.subplot(3, 3, 6)
sns.scatterplot(data=df, x='age', y='salary', hue='department', 
                palette='deep', s=100, alpha=0.7)
plt.title('Yosh va Maosh O\'rtasidagi Bog\'liqlik', fontsize=14, fontweight='bold')
plt.xlabel('Yosh', fontsize=11)
plt.ylabel('Maosh ($)', fontsize=11)
plt.legend(title='Department', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.subplot(3, 3, 7)
sns.violinplot(data=df, x='department', y='performance_rating', palette='muted')
plt.title('Ish Samaradorligi - Departmentlar Bo\'yicha', fontsize=14, fontweight='bold')
plt.xlabel('Department', fontsize=11)
plt.ylabel('Performance Rating', fontsize=11)
plt.xticks(rotation=45)

plt.subplot(3, 3, 8)
sns.countplot(data=df, x='department', palette='Set3', order=df['department'].value_counts().index)
plt.title('Xodimlar Soni - Departmentlar Bo\'yicha', fontsize=14, fontweight='bold')
plt.xlabel('Department', fontsize=11)
plt.ylabel('Xodimlar Soni', fontsize=11)
plt.xticks(rotation=45)
for i, v in enumerate(df['department'].value_counts().values):
    plt.text(i, v + 0.2, str(v), ha='center', fontweight='bold')

plt.subplot(3, 3, 9)
numeric_cols = df[['age', 'salary', 'performance_rating']].corr()
sns.heatmap(numeric_cols, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Korrelyatsiya Matritsasi', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('employee_dashboard.png', dpi=300, bbox_inches='tight')
print("\n✅ Dashboard saqlandi: employee_dashboard.png")
plt.show()
