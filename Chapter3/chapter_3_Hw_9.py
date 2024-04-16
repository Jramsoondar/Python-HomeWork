'''Write a program that receives a series of numbers from the user and allows the 
user to press the enter key to indicate that he or she is finished providing inputs. 
After the user presses the enter key, the program should print the sum of the 
numbers and their average'''

def main():
    THE_SUM = 0.0
    COUNT = 0
    calc_sum_average(THE_SUM,COUNT)
def calc_sum_average(THE_SUM,COUNT):
    numbers= input('Enter the Numbers or press enter to End ')
    while numbers !="":
        sum_of_num = float(numbers)
        THE_SUM += sum_of_num
        COUNT += 1
        numbers = input('Enter the Numbers or press enter to End ')
    print('The sum of the numebers is: ', THE_SUM)
    average = THE_SUM / COUNT
    print('The average is: ', average)
main()