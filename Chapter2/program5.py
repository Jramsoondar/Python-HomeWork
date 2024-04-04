"""An object’s momentum is its mass multiplied by its velocity. Write a program 
that accepts an object’s mass (in kilograms) and velocity (in meters per second) as 
inputs and then outputs its momentum."""
massNumber = float(input('What is the mass: '))
velocityNumber = float(input('What is the velocity: '))
momentumTotal = massNumber * velocityNumber 
print('The total momentum is: ', momentumTotal)