import pandas as pd

# Load
df = pd.read_csv("/Users/akhmadalievruziboy/Desktop/GitHub/NumPy/Pandas/Lesson-7.0.py/US_Top_50_Universities_2026.csv")

# Clean column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Remove duplicates
df = df.drop_duplicates()

# Fix data types
df["founded_year"] = df["founded_year"].astype(int)

# Check missing values
print("Missing values:\n", df.isna().sum())

# Save
df.to_csv("universities_cleaned.csv", index=False)
print("✅ Done! Shape:", df.shape)