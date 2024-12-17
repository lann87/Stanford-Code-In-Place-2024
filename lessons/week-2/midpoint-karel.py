from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""
def main():
#Detection of 2x2 and sequence for it.
    move()
    if front_is_blocked():
        turn_back()
        move()
        turn_back()
        put_beeper()
#Main bulk of Karel's movement and tracking
    else:    
        put_two()
        wall_to_wall()
        while beepers_present() and beepers_in_bag():
            beep()
            move_to_beep()
        end_beep()

#Karel's general direction FN.
def move_to_beep():
    if front_is_clear():
        move()
    while no_beepers_present() and front_is_clear():
        move()
    turn_back()

def turn_back():
    for b in range(2):
        turn_left()

def move_fwd():
    while front_is_clear():
        move()

#Beeper placing and tracking mechanism FN.
def end_beep():
    move()
    if front_is_clear():    
        while no_beepers_present():
            move()
        if beepers_present():
            pick_beeper()
            if facing_west():
                while front_is_clear():
                    move()
                turn_back()
                while no_beepers_present():
                    move()
    else:
        pick_beeper()
        turn_back()
        move()
        turn_back()

def beep():
    if beepers_present():
        pick_beeper()
        move()    
        put_beeper()

#Karel's starting move FN.
def put_two():
    move_fwd()
    put_beeper()
    turn_back()
    move_fwd()
    put_beeper()

def wall_to_wall():
    turn_back()
    move_fwd()
    turn_back()

if __name__ == '__main__':
    main()