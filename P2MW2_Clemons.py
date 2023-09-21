#CTI 110
#P2HW2 - List
#Clemons
#9/21/23

print("Enter your grade for Module 1:")

grade1 = float(input())
print("Enter your grade for Module 2:")
grade2 = float(input())
print("Enter your grade for Module 3:")
grade3 = float(input())
print("Enter your grade for Module 4:")
grade4 = float(input())
print("Enter your grade for Module 5:")
grade5 = float(input())
print("Enter your grade for Module 6:")
grade6 = float(input())

grades = [grade1, grade2, grade3, grade4, grade5, grade6]

print(f"Lowest grade: {min(grades)}")
print(f"Lowest grade: {max(grades)}")

all_scores = sum(grades)
print("Sum of grades:", all_scores)
average = all_scores / len(grades)
print("Avergae:", f"{average:.2f}")

      


