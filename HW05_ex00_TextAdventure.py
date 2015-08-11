#!/usr/bin/env python
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
import sys

# Body


def infinite_stairway_room(user_name, count=0):
    print user_name + " walks through the door to see a dimly lit hallway."
    print "At the end of the hallway is a", count * 'long ', 'staircase going towards some light'
    next = raw_input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print user_name + ' takes the stairs'
        if (count > 0):
            print "but " + user_name + " is not happy about it"
        infinite_stairway_room(count + 1)
    if next == "curl up and die":
        dead(user_name + " gave up on the stairs!")


def gold_room(user_name):
    print "This room is full of gold.  How much does " + user_name + " take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, " + user_name + " you're not greedy, you win!"
        exit(0)
    else:
        dead(user_name + " is a greedy bastard!")


def bear_room(user_name):
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")
        print bear_moved
        if next == "take" or next == "honey":
            dead("The bear looks at " + user_name + " then slaps their face off.")
        
        elif next == "taunt" and not bear_moved:
            print "The bear has moved from the door. " + user_name + " can go through it now."
            bear_moved = True
        
        elif next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        
        elif (next == "open" or next == "door") and bear_moved:
            gold_room(user_name)

        else:
            print "I got no idea what that means."


def cthulhu_room(user_name):
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at " + user_name + " and eats their head off."
    print "Does " + user_name + " flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        infinite_stairway_room(user_name)


def dead(why):
    print why, "Good job!"
    exit(0)


##############################################################################
def main():
    # START the TextAdventure game
    user_name = sys.argv[1]
 
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take, " + user_name + "?"

    next = raw_input("> ")

    if next == "left":
        bear_room(user_name)
    elif next == "right":
        cthulhu_room(user_name)
    else:
        dead("You stumble around the room until you starve.")

if __name__ == '__main__':
    main()
