
print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))
mark4 = float(input("Enter marks for Subject 4: "))
mark5 = float(input("Enter marks for Subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5

percentage = total / 5

print("\n===== RESULT =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")

if percentage >= 90:
    print("Grade: A")

elif percentage >= 75:
    print("Grade: B")

elif percentage >= 60:
    print("Grade: C")

elif percentage >= 40:
    print("Grade: D")

else:
    print("Grade: Fail")
