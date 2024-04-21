'''The Payroll Department keeps a list of employee information for each pay period 
in a text file. The format of each line of the file is the following:
<last name> <hourly wage> <hours worked>
Write a program that inputs a filename from the user and prints to the terminal a 
report of the wages paid to the employees for the given period. The report should 
be in tabular format with the appropriate header. Each line should contain an 
employee’s name, the hours worked, and the wages paid for that period.'''
try:
    # Open the file entered by the user for reading
    filename = input('Enter the file name: ')
    with open(filename, 'r') as file:
        for line in file:
            data = line.split()
            if len(data) == 3:
                last_name, hourly_wage, hours_worked = data
                wages_paid = float(hourly_wage) * float(hours_worked)
                print("last_name\thours_worked\twages_paid")
            else:
                print("Invalid data format in file:", line)
except FileNotFoundError:
    print('File not found')
print("Employee Name\tHours Worked\tWages Paid")
print("--------------------------------------------")