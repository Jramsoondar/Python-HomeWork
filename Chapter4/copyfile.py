'''Write a script named copyfile.py. This script should prompt the user for the 
names of two text files. The contents of the first file should be input and written 
to the second file.'''
fileName = input('Enter the file name: ')
fileName_two = input('Enter the Second file name: ')
try:
    with open("fileName", 'r') as file1:
        contents = file1.read()
        with open('fileName_two', 'w') as file2:
            file2.write(contents)
except FileNotFoundError:
    print('File not found')
