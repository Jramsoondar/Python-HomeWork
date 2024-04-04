'''An employee’s total weekly pay equals the hourly wage multiplied by the total 
number of regular hours plus any overtime pay. Overtime pay equals the total 
overtime hours multiplied by 1.5 times the hourly wage. Write a program that 
takes as inputs the hourly wage, total regular hours, and total overtime hours and 
displays an employee’s total weekly pay'''
regularHours = int(input('Enter the Number of hours you worked'))
overTimeHours = int(input('Enter the amount of overtime you worked'))
hourlyWage = float(input('How much do you make an hour'))

regularPay = regularHours * hourlyWage
overTimePay = (hourlyWage * 1.5) * overTimeHours
totalPay = regularPay + overTimePay

print('Your total pay is', totalPay , '$')