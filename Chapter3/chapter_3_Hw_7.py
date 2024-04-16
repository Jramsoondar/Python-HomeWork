'''Teachers in most school districts are paid on a schedule that provides a salary 
based on their number of years of teaching experience. For example, a beginning 
teacher in the Lexington School District might be paid $30,000 the first year. For 
each year of experience after this first year, up to 10 years, the teacher receives a 
2% increase over the preceding value. Write a program that displays a salary schedule, in tabular format,
for teachers in a school district. The inputs are the starting 
salary, the percentage increase, and the number of years in the schedule. Each row 
in the schedule should contain the year number and the salary for that year'''

def main():
    salary_yearly = float(input('What is your starting yearly salary? '))
    percentageInc= float(input('How much did you increase? '))
    years_of_experience = int(input('How many years have you worked here? '))
    calc_salary(salary_yearly,percentageInc,years_of_experience)
    
def calc_salary(salary_yearly,percentageInc,years_of_experience):
    print("Salary\tYears")

    for years in range(1, years_of_experience + 1):
        salary_yearly = salary_yearly * (1 + percentageInc / 100)
        salary_yearly = round(salary_yearly,2)
        print(f'{years}\t${salary_yearly}')
    

main()

