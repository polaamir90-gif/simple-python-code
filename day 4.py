n=int(input("Enter the number of students :"))

degrees=[]

for degree in range(n) :
   y=int(input("Enter the degrees :"))
   degrees.append(y)
degrees.sort(reverse=True)
print(f"Degrees : {degrees}")

"""max_degrees=max(degrees)
print(f"Max Degrees : {max_degrees}")

min_degrees=min(degrees)
print(f"Min Degrees : {min_degrees}")"""

max_degree = degrees[0]
print(f"Max Degrees : {max_degree}")

min_degree = degrees[1]
print(f"Min Degrees : {min_degree}")