
import csv
import os

FILE = "attendance.csv"

def add_student():
    name = input("Enter student name: ")
    usn = input("Enter USN: ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, usn, "Not Marked"])

    print("Student added successfully!")

def mark_attendance():
    if not os.path.exists(FILE):
        print("No students found!")
        return

    students = []

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        students = list(reader)

    usn = input("Enter student USN: ")
    found = False

    for student in students:
        if len(student) == 3 and student[1] == usn:
            student[2] = input("Enter Present/Absent: ").capitalize()
            found = True
            break

    if found:
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(students)
        print("Attendance updated!")
    else:
        print("Student not found!")

def view_attendance():
    if not os.path.exists(FILE):
        print("No records found!")
        return

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

while True:
    print("\n--- Student Attendance System ---")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        view_attendance()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
