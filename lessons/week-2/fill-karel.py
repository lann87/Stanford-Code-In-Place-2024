from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

def main():
    while left_is_clear():
        beep()
        move_up()
    fin_beep()

# One beep does most of the map and the other handle only the last row's
def beep():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    uturn()

def fin_beep():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

# Movement FN

def uturn():
    for u in range(2):
        turn_left()
    while front_is_clear():
        move()

def turn_right():
    for r in range(3):
        turn_left()

def move_up():
    turn_right()
    move()
    turn_right()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()