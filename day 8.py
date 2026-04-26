"""
names = ["Ahmed", "Mohamed", "Ali", "Sara", "Mona"]
scores = [85, 92, 45, 78, 60]

grad = list(zip(names, scores))

passed = list(filter(lambda x: x[1] >= 60, grad))

sorted_list = sorted(passed, key=lambda x: x[1], reverse=True)

print(sorted_list)
"""
##########################################################

names  = ["Ahmed", "Mohamed", "Ali", "Sara", "Mona"]
scores = [95, 85, 45, 75, 60]
GPA = list(map(lambda x : (x / 100) * 4.0  ,scores))
List1 = list(zip(names,scores,GPA))
passed = list(filter(lambda x :x[1] >=60 ,List1))
FinalList= list(sorted(passed , key= lambda  x : x[1], reverse=True))
print("\n--- Results ---")
for name, score, gpa in FinalList:
    print(f"{name:<10} | Score: {score} | GPA: {gpa:.2f}")