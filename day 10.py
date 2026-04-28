import csv
path = r"E:\dream\pythonProject3\students.csv"
while True:
    print("\n=== Student Manager ===")
    print("1 - Add Student")
    print("2 - Show Report")
    print("3 - Exit")
    choice = input("Choose: ")

    if choice == "1":
        while True:
            name = input("Enter name (or 'done' to stop): ")
            if name.lower() == 'done':
                break
            try:
               score = int(input("Enter score: "))
               if score < 0 or score > 100:
                   print("Score must be 0-100!")
               else:
                 with open(path, "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([name, score])
                 print("Saved! ✅")
            except ValueError:
                print("Invalid score!")


    elif choice == "2":

        try:

            all_students = []

            with open(path, "r") as f:

                reader = csv.reader(f)

                for row in reader:
                    all_students.append((row[0], int(row[1])))

            print("\n--- All Students ---")

            for name, score in all_students:
                print(f"{name:<10} | {score}")

            passed = [(n, s) for n, s in all_students if s >= 60]

            print("\n--- Passed ---")

            for name, score in passed:
                print(f"{name:<10} | {score}")

            scores = [s for _, s in all_students]

            average = sum(scores) / len(scores)

            top = max(all_students, key=lambda x: x[1])

            print(f"\nAverage: {average:.1f}")

            print(f"Top Student: {top[0]} | {top[1]}")


        except FileNotFoundError:

            print("No students yet!")

    elif choice == "3":
        print("Bye")
        break


