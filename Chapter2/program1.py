"""The tax calculator program of the case study outputs a floating-point number 
that might show more than two digits of precision. Use the round function to 
modify the program to display at most two digits of precision in the output 
number."""
totalGross = float(input("Enter the gross income: "))
depndentNumber = int(input('Enter the number of dependents: '))

TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

afterTaxed = totalGross - STANDARD_DEDUCTION -  DEPENDENT_DEDUCTION * depndentNumber
incomeTax = afterTaxed * TAX_RATE
taxedTotal = round(incomeTax,2)

print('The income tax is $' + str(taxedTotal))