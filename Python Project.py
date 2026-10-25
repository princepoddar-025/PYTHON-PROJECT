# PROJECT 1

balance = 10000
correct_pin = 1234
attempts = 0

while attempts < 3:
    userpin = int(input("Enter your pin: "))
    if userpin == correct_pin:
        while True:
         print("1.Balance")
         print("2.deposit")
         print("3.Withdraw")
         print("4.Exit")
         service = int(input("Select service: "))
         if service == 1:
                  print(f"your balance is {balance}")
         elif service == 2:
                  amount = int(input("Enter amount to deposit: "))
                  balance += amount
                  print(f"your new balance is {balance}")
         elif service == 3:
                  amount = int(input("Enter amount to withdraw: "))
                  if amount <= balance:
                    balance -= amount
                    print(f"your new balance is {balance}")
                  else:
                    print("Insufficient funds")
         elif service == 4:
                  print("Thank you for using our service")
                  break
         else:
              print ("Enter a valid service")
              
        break
    else:
        attempts += 1
        if attempts < 3:
            print("Invalid Pin, try again")
            
else:
    print("Card Blocked")


# PROJECT 2


students = {
    "Aman": [85, 90, 78],
    "Riya": [92, 88, 95],
    "Zoya": [70, 65, 80]
}

averages = {}
grades = {}

# Stage 1 and Stage 2: Averages and Grades
for name in students:
    marks = students[name]
    average = round(sum(marks) / 3, 2)
    averages[name] = average

    if average >= 85:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "F"

    grades[name] = grade
    print(name, average, grade)

# Stage 3: Find Topper
topper = ""
highest = -1

for name in averages:
    if averages[name] > highest:
        highest = averages[name]
        topper = name

print("Topper:", topper)

# Stage 4 and Stage 5: Menu and Validation
while True:
    print("\n1. Add student")
    print("2. View all")
    print("3. Show topper")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ").strip()

        if name in students:
            print("Student already exists.")
            continue

        marks = []

        while len(marks) < 3:
            mark = input("Enter mark (0-100): ")

            if not mark.isdigit() or int(mark) < 0 or int(mark) > 100:
                print("Invalid mark, try again.")
            else:
                marks.append(int(mark))

        students[name] = marks

        average = round(sum(marks) / 3, 2)
        averages[name] = average

        if average >= 85:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 50:
            grade = "C"
        else:
            grade = "F"

        grades[name] = grade
        print("Student added successfully.")

    elif choice == "2":
        for name in students:
            print(name, averages[name], grades[name])

    elif choice == "3":
        topper = ""
        highest = -1

        for name in averages:
            if averages[name] > highest:
                highest = averages[name]
                topper = name

        print("Topper:", topper)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")