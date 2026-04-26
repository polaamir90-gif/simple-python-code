"""
def calc_bmi(weight, height):
    bmi = weight / (height ** 2)

    if 18.5 < bmi <= 24.9:
        status = "Normal"
    elif bmi > 24.9:
        status = "Overweight"
    else:
        status = "Underweight"

    return bmi, status


bmi, status = calc_bmi(70, 1.75)
print(f"BMI: {bmi:.2f}")
print(f"Status: {status}")
"""
from itertools import count

#######################################################################
"""
def get_grade(degrees) :
    if 90 <= degrees < 100:
        status = "A"
    elif 80 <= degrees <= 89:
        status = "B"
    elif 70 <= degrees <= 79:
        status = "C"
    elif 60 <= degrees <= 69:
        status = "D"
    else:
        status = "F"

    return degrees ,status

degrees,status = get_grade(82)
print(f"Degrees is {degrees} ")
print(f"Grade : {status}")
"""
#######################################################################
"""
def analyze_list (numbers) :
   total = sum(numbers)

   if len(numbers)>0 :
       average = total / len(numbers)
   else:
       print("Error")

   maximum = max(numbers)

   minimum = min(numbers)

   return total , average , maximum , minimum

numbers = [10, 20, 30, 40, 50]
total, average, maximum, minimum = analyze_list(numbers)

print("\n--- Report ---")
print(f"Total : {total}")
print(f"Average : {average}")
print(f"Maximum  : {maximum }")
print(f"Minimum : {minimum}")
"""
#######################################################################
def get_report(students) :
    if len(students) == 0:
        return None

    count1=0
    count2=0

    scores = []
    for student in students:
        score = student[1]
        scores.append(score)

        if score >60:

            count1+=1
        else:
            count2+=1

    total = sum(scores)
    average = total / len(scores)
    maximum = max(scores)
    minimum = min(scores)

    return total, average, maximum, minimum, count1, count2

students = [
    ("Pola", 85),
    ("Mon", 92),
    ("Meko", 60),
    ("Ham", 45),
    ("Said", 78)
]

total, average, maximum, minimum , count1 ,count2 = get_report(students)

print("\n--- Report ---")
print(f"Total : {total}")
print(f"Average : {average}")
print(f"Maximum : {maximum }")
print(f"Minimum : {minimum}")
print(f"Passed  : {count1}")
print(f"Failed  : {count2}")