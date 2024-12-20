from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    build_pillar()
    while front_is_clear():
        move()
        build_pillar()

# Pillar building function.
def build_pillar():
    turn_left()
    put_beeper()
    for beep in range(4):
        move()
        put_beeper()
    if front_is_blocked():
        move_down()
    else:
        remove_beep()

# Will proceed to remove pillar when ceiling is higher than expected.
def remove_beep():
    turn_back()
    pick_beeper()
    for rbeep in range(4):
        move()
        pick_beeper()
    turn_left()

# Movement controller - Up, Right.
def move_down():
    turn_back()
    while front_is_clear():
        move()
    turn_left()

def turn_back():
    for b in range(2):
        turn_left()

def turn_right():
    for r in range(3):
        turn_left()

if __name__ == '__main__':
    main()