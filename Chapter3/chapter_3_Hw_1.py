'''Write a program that accepts the lengths of three sides of a triangle as inputs. 
The program output should indicate whether or not the triangle is an equilateral 
triangle.'''


def main():
    triangle_side_A = int(input("What are the length of the triangle side A "))
    triangle_side_B = int(input("What are the length of the triangle side B "))
    triangle_side_C = int(input("What are the length of the triangle side C "))
    triangle(triangle_side_A,triangle_side_B,triangle_side_C)

def triangle(triangle_side_A,triangle_side_B,triangle_side_C):
    if triangle_side_A != triangle_side_B != triangle_side_C:
        print('This is not an equilateral triangle')
    else:
     triangle_side_A == triangle_side_B == triangle_side_C
    print('This is an equilateral triangle')
main()
