"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

def main():
    print("This program multiplies two numbers.")
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    # Multiplies the input of first & second and print it out.
    print(first*second)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()