# CTI-110
# Clemons


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules


print("Enter grades for six modules")
mod_1 = float(input())
mod_2 = float(input())
mod_3 = float(input())
mod_4 = float(input())
mod_5 = float(input())
mod_6 = float(input())



# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = sum(grades)
avg = sum / len(grades)
# TO DO: print lowest, highest, sum and average for grades
print("Lowest grade:", low)
print("Highest grade:", high)
print("Sum of grades:", sum)
print("Average of grades:", avg)





# determine letter grade for average


if avg >= 90:
 print('Your grade is: A')
elif avg > 80:
  print('Your grade is: B')
  
elif avg > 70:
  print('Your grade is: C')
  
elif avg > 60:
  print('Your grade is: D')
  
else:
  print('Your grade is: F')
  
   








