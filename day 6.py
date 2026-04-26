n = int(input("Enter number of students: "))

students = []

for i in range(n):
    name = input("Enter name: ")
    degree = int(input("Enter degree: "))

    if 0 <= degree <= 100:
        students.append((name, degree))

degrees = [d for name, d in students]

results = ["Pass" if d >= 50 else "Fail" for d in degrees]

labels = ["Excellent" if d >= 85 else "Good" if d >= 65 else "Fail" for d in degrees]

bonus = [min(d + 5, 100) for d in degrees if d >= 50]

print("\n--- Report ---")

if len(degrees) > 0:
    avg = sum(degrees) / len(degrees)
    print(f"Average: {avg}")
    print(f"Max: {max(degrees)}")
    print(f"Min: {min(degrees)}")
else:
    print("No valid data")

print(f"Students: {students}")
print(f"Results: {results}")
print(f"Labels: {labels}")
print(f"Bonus: {bonus}")