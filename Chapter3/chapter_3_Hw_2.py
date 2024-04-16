'''Write a program that accepts the lengths of three sides of a triangle as inputs. 
The program output should indicate whether or not the triangle is a right triangle. Recall from the Pythagorean theorem that in a right triangle, the square of 
one side equals the sum of the squares of the other two sides.'''
def main():
    triangle_side_A = int(input("What are the length of the triangle side A "))
    triangle_side_B = int(input("What are the length of the triangle side B "))
    triangle_side_C = int(input("What are the length of the triangle side C "))
    right_triangle(triangle_side_A,triangle_side_B,triangle_side_C)


def right_triangle(triangle_side_A,triangle_side_B,triangle_side_C):
    if triangle_side_A ** 2 + triangle_side_B ** 2 == triangle_side_C ** 2:
        print('This is an right triangle')
    elif triangle_side_C ** 2 + triangle_side_A ** 2 == triangle_side_B ** 2:
        print('This is an right triangle')
    elif triangle_side_B ** 2 + triangle_side_C ** 2 == triangle_side_A ** 2:
        print('This is an right triangle')
    else:
        print('This is not an right triangle')
        
main()