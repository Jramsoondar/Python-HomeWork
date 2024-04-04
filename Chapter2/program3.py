'''Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who 
like to buy LP record albums. The store rents new videos for $3.00 a night, and 
oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video 
can use to calculate the total charge for a customer’s video rentals. The program 
should prompt the user for the number of each type of video and output the total 
cost'''
VSH_TAPES_OLD = 2.00
VSH_TAPES_NEW = 3.00

numberOfOld = int(input("How many old video do you want: " ))
numberOfNew = int(input('How many new videos do you want: '))

totalOld = numberOfOld * VSH_TAPES_OLD
totalNew = numberOfNew * VSH_TAPES_NEW
total = totalNew + totalOld
print('The total cost is ', total, '$')
