n = int(input("Enter number of students: "))

degrees = []

for i in range(n):
    degree = int(input("Enter degree: "))
    degrees.append(degree)

clean_degrees = [d for d in degrees if 0 <= d <= 100]

passed = [d for d in clean_degrees if d >= 50]
failed = [d for d in clean_degrees if d < 50]

if len(clean_degrees) > 0:
    total = sum(clean_degrees)
    avg = total / len(clean_degrees)

else:
    print("No valid data entered")



print("\n--- Report ---")
print(f"Correct degrees: {clean_degrees}")
print(f"Average: {avg}")
print(f"passed degrees: {passed}")
print(f"failed degrees: {failed}")
print(f"Number of student passed exam {len(passed)}")
print(f"Number of student failed exam {len(failed)}")