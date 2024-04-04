'''Write a program that takes the radius of a sphere (a floating-point number) as 
input and then outputs the sphere’s diameter, circumference, surface area, and 
volume.'''
radiusNumber = float(input('What is the radius of the sphere? '))
NUMBER_PI = 3.14
sphereDiameter = 2 * radiusNumber
sphereCircumference = 2 * NUMBER_PI * radiusNumber
sphereSurfaceArea = NUMBER_PI * 4 * radiusNumber ** 2 
sphereVolume = (4 / 3) * NUMBER_PI * radiusNumber ** 3  

print('The sphere diameter is', sphereDiameter)
print('The sphere circumference is', sphereCircumference)
print('The sphere surface area is ', sphereSurfaceArea)
print('The sphere volume is ', sphereVolume)