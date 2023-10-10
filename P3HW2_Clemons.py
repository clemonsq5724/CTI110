
#Asks the user to enter name of employee
name = input("Enter employee's name: ")



#Ask user to enter number of hours the employee worked this week
hours = float(input("Enter number of hours worked this week: "))
#Ask user to enter employee's pay rate
pay_rate = float(input("Enter employee's pay rate: "))
#Evaluate if employee has worked overtime (more than 40 hours). If yes, calculate the amount owed to employee for overtime hours
if hours > 40:
  overtime_hours = hours - 40
else: 
  overtime_hours = 0
  
#Calculate amount employee should be paid for regular hours worked.
regular_pay = hours * pay_rate
overtime_pay = overtime_hours * (pay_rate * 1.5)

#Display gross pay (total amount that should be paid to employee)
gross_pay = regular_pay + overtime_pay
print("Employee's gross pay: $", gross_pay)
#Display all on one line, (name, pay rate, hours worked, overtime hours, overtime pay, and regular hours and gross pay)
print("Name", 'Rate', 'Hours', 'OT hrs', 'OT pay', 'Reg_pay', 'Gross_pay', sep = "\t")
print(name, pay_rate, hours, overtime_hours, overtime_pay, regular_pay, gross_pay, sep = "\t")


  



    
