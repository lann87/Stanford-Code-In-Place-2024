import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    """
    You should write your code here. Make sure to delete 
    the 'pass' line before starting to write your own code.
    """
    for r in range (10):
        num = random.randint(1, 100)
        print(num)

if __name__ == '__main__':
    main()