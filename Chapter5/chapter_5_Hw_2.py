'''Write a program that allows the user to navigate the lines of text in a file. The 
program should prompt the user for a filename and input the lines of text into a 
list. 
The program then enters a loop in which it prints the number of lines in the 
file and prompts the user for a line number. Actual line numbers range from 1 to 
the number of lines in the file. If the input is 0, the program quits. Otherwise, the 
program prints the line associated with that number'''
def main():
    filename = input("Enter the filename: ")
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            num_lines = len(lines)
            print(f"Total lines in {filename}: {num_lines}")

            while True:
                line_number = int(input("Enter a line number (1 to quit, 0 to exit): "))
                if line_number == 0:
                    break
                elif 1 <= line_number <= num_lines:
                    print(f"Line {line_number}: {lines[line_number - 1].strip()}")
                else:
                    print("Invalid line number. Please try again.")
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please check the filename and try again.")

if __name__ == "__main__":
    main()