from karel.stanfordkarel import *

def main():
# each time it detects beeper = move forward.
    while beepers_present():
        move()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()