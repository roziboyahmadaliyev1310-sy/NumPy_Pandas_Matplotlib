import pandas as pd

# Data cleaning = the process of fixing/removing:
#                   inomplete, incorrect or irrelevent data.
#                   ~75% of work done with Pandas is data cleaning 


# STEP.1 - Load and Inspect first

df=pd.read_csv('/Users/akhmadalievruziboy/Desktop/GitHub/NumPy/Pandas/Lesson-7.0.py/US_Top_50_Universities_2026.csv')

#  qatorlar va ustunlar soni
print(df.shape)

# birinchi 5 qator
print(df.head())

# ma'lumot turlari
print(df.info())

# statistika
print(df.describe())


# STEP.2 - CHECK MISSING VALUES

# har ustundagi bo'sh qiymatlar
print(df.isna().sum())

# jami bo'sh qiymatlar soni
print(df.isna().sum().sum())


# STEP.3 - CHECK DUPLICATES

print('Duplicates: ',df.duplicated().sum())

# Remove duplicates
df=df.drop_duplicates()
print("After removing duplicates:", df.shape)

# Make all column names lowercase and replace spaces with underscore
df.columns = df.columns.str.lower().str.replace(" ", "_")
print(df.columns.tolist())

print(df.dtypes)

# Founded_Year should be int, not float
df["founded_year"] = df["founded_year"].astype(int)

print(df.dtypes)

# Check min and max values
print(df[["research_impact_score", "intl_student_ratio", "employment_rate"]].describe())

# Find universities with very low research score
low_research = df[df["research_impact_score"] < 40]
print("\nLow research score universities:")
print(low_research[["university_name", "research_impact_score"]])

print(df["institution_type"].value_counts())

# Separate public and private
public = df[df["institution_type"] == "Public"]
private = df[df["institution_type"] == "Private"]

print("Public universities:", len(public))
print("Private universities:", len(private))

df.to_csv("universities_cleaned.csv", index=False)
print("✅ Cleaned file saved!")






# df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# # 1. Drop irrelevent columns
# df=df.drop(columns=['PassengerId','Survived','Embarked'])

# # 2. Handle missing value
# df=df.dropna(subset=['Cabin'])

# # fillna = is used to change NaN
# df=df.fillna({'Cabin': 'NoNe'})


# print(df)

