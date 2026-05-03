import pandas as pd
import numpy as np

data = {
    "Name":   ["Ahmed", "mohamed", "  Ali  ", "Sara", "Ahmed", None],
    "Score":  [85, 92, None, 45, 85, 78],
    "Age":    [20, 22, 19, None, 20, 25],
    "City":   ["Cairo", "cairo", "Alex", "CAIRO", "Cairo", "Alex"],
    "Salary": ["5000", "7000", "4500", None, "5000", "6000"]
}

df = pd.DataFrame(data)

print(df.isnull().sum())
df["Score"] = df["Score"].fillna(df["Score"].mean())
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(0).astype(int)
df = df.dropna(subset=["Name"])
df["Name"] = df["Name"].str.strip().str.title()
df["City"] = df["City"].str.lower()
df["Salary"] = df["Salary"].astype(int)
df = df.drop_duplicates()
print(f" ### Data after clean ### ")
print(df)
