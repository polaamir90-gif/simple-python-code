import pandas as pd
import numpy as np


data = {
    "Name":       ["Ahmed", "Mohamed", "Ali", "Sara", "Mona",
                   "Karim", "Nour", "Omar"],
    "Math":       [85, 92, 60, 45, 78, 88, 55, 91],
    "Science":    [90, 88, 55, 50, 82, 79, 60, 95],
    "English":    [78, 95, 70, 40, 75, 85, 65, 88],
    "Attendance": [95, 80, 60, 40, 90, 85, 70, 92]
}
df = pd.DataFrame(data)
shape=df.shape
print(f"Shape: {shape}")
df.info()
result = df[df['Math'] > 80][['Name', 'Math']]
print("=== Math > 80 ===")
print(result)
result2= df[df['Attendance'] < 70][['Name','Attendance']]
print("=== Low Attendance ===")
print(result2)

stats = df[['Math', 'Science', 'English']].describe()

print(stats)

df['Average']=df[['Math', 'Science', 'English']].mean(axis=1)

df['Status'] = np.where(df['Average'] >= 60, 'Pass', 'Fail')
print(df)


df = df.sort_values(by='Average', ascending=False)
print(df[['Name', 'Average']])

passed_count = (df['Status'] == 'Pass').sum()
failed_count = (df['Status'] == 'Fail').sum()

print(f"\nNumber of Passed students: {passed_count}")
print(f"Number of Failed students: {failed_count}")