"""You can calculate the surface area of a cube if you know the length of an edge. 
Write a program that takes the length of an edge (an integer) as input and prints 
the cube’s surface area as output."""
numberOne = int(input('Insert a number'))
totalSurfaceArea = 6 * numberOne ** 2
print(f'The total surface area is {totalSurfaceArea}')