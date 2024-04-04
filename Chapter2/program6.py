'''The kinetic energy of a moving object is given by the formula KE 1 2/ mv 5 2 ( )
where m is the object’s mass and v is its velocity. Modify the program you created 
in Project 5 so that it prints the object’s kinetic energy as well as its momentum.'''
massNumber = float(input('What is the mass: '))
velocityNumber = float(input('What is the velocity: '))
momentumTotal = massNumber * velocityNumber 
keneticEnergy = (1/2) * massNumber * velocityNumber ** 2
print('The total momentum is: ', momentumTotal,'and the total kenetic energy is:', keneticEnergy)