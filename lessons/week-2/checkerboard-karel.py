from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""
'''
Created odd(start) and even beeper row fills and when they hit the ceiling
that will trigger the end of the loop via either odd_end or even_end.

'''
def main():
    if front_is_blocked() and right_is_blocked():
        put_beeper()
        if left_is_clear():
            turn_left()
        while front_is_clear():
            move()
            if front_is_clear():
                move()
            put_beeper()
        turn_back()

    else:
        while left_is_clear() and no_beepers_present():
            odd()
            even()

# this will activate on every odd row including the start.
def odd():
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    turn_back()

#  this will trigger when it reaches the ceiling
def odd_end():
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
    if front_is_blocked():
        put_beeper()
    turn_back()

# this is will activate on each even row.
def even():
    move()
    while front_is_clear():
        put_beeper()
        if front_is_clear():
            move()
            if front_is_blocked():
                turn_back()
            else:
                move()
    if front_is_blocked():
        put_beeper()
    turn_back()

#  this will trigger when it reaches the ceiling
def even_end():
    move()
    while front_is_clear():
        put_beeper()
        move()
        if front_is_clear():
            move()
    if front_is_blocked():
        put_beeper()
    turn_back()


# General Movement

def turn_back():
    for b in range(2):
        turn_left()
    while front_is_clear():
        move()
    if right_is_blocked():
        turn_left()
        while front_is_clear():
            move()
        if front_is_blocked() and facing_south():
            turn_left()
    else:
        move_up()

def move_up():
    if front_is_blocked():
        turn_right()
        move()
        turn_right()

def turn_right():
    for r in range(3):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()